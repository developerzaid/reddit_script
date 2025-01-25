# main.py

import praw
import time
import random

from creds import ACCOUNTS
from configurations import (
    SUBREDDITS,
    KEYWORDS,
    LIMIT_PER_KEYWORD,
    DAILY_SEND_LIMIT
)
from helpers import load_messaged_authors
from sender import send_daily_messages_for_account


def gather_potential_authors(reddit, subreddits, keywords, limit_per_keyword, already_messaged):
    """
    Perform searches on the specified subreddits, using the given keywords.
    Returns a list of authors (usernames as strings) who have NOT been messaged yet.
    """
    found_authors = set()

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for kw in keywords:
            # Search with a small limit to avoid heavy API usage
            for submission in subreddit.search(kw, sort="new", limit=limit_per_keyword):
                if submission.author is None:
                    continue

                author_str = str(submission.author).lower()
                # Only add if not already messaged
                if author_str not in already_messaged:
                    found_authors.add(author_str)

    return list(found_authors)


def main():
    # Load authors we've already messaged
    already_messaged = load_messaged_authors()

    while True:
        # Use the first account's credentials to do the searching
        search_reddit = praw.Reddit(
            client_id=ACCOUNTS[0]["client_id"],
            client_secret=ACCOUNTS[0]["client_secret"],
            user_agent=ACCOUNTS[0]["user_agent"],
            username=ACCOUNTS[0]["username"],
            password=ACCOUNTS[0]["password"]
        )

        print("\n[INFO] Gathering new authors for the day...")
        daily_authors_pool = gather_potential_authors(
            reddit=search_reddit,
            subreddits=SUBREDDITS,
            keywords=KEYWORDS,
            limit_per_keyword=LIMIT_PER_KEYWORD,
            already_messaged=already_messaged
        )

        print(f"[INFO] Found {len(daily_authors_pool)} potential authors (not yet messaged).")

        if not daily_authors_pool:
            print("[INFO] No new authors found. Sleeping 24 hours...")
            time.sleep(24 * 3600)
            continue

        # Shuffle so we don't message them in the same order all the time
        random.shuffle(daily_authors_pool)

        # Split the authors among all accounts
        chunked_authors = []
        start_index = 0
        for _ in ACCOUNTS:
            end_index = start_index + DAILY_SEND_LIMIT
            chunk = daily_authors_pool[start_index:end_index]
            chunked_authors.append(chunk)
            start_index = end_index

        # Each account sends messages to its chunk
        for i, account in enumerate(ACCOUNTS):
            account_authors = chunked_authors[i]
            if not account_authors:
                print(f"[{account['username']}] No authors available to message.")
                continue

            print(f"\n[INFO] Logging in and sending messages for {account['username']}...")
            send_daily_messages_for_account(
                account=account,
                daily_authors=account_authors,
                already_messaged=already_messaged
            )

        print("[INFO] Daily messaging cycle completed. Sleeping 24 hours until next day...")
        time.sleep(24 * 3600)


if __name__ == "__main__":
    main()
