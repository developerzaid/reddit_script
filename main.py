import praw
import time
import random
from helpers import *
from configurations import *
from creds import *
from sender import send_daily_messages_for_account


def main():
    already_messaged = load_messaged_authors()

    while True:
        search_reddit = praw.Reddit(
            client_id=ACCOUNTS[0]["client_id"],
            client_secret=ACCOUNTS[0]["client_secret"],
            user_agent=ACCOUNTS[0]["user_agent"],
            username=ACCOUNTS[0]["username"],
            password=ACCOUNTS[0]["password"]
        )

        # Select 10 random subreddits & 5 random keywords daily

        daily_subreddits = random.sample(SUBREDDITS, min(10, len(SUBREDDITS)))
        daily_keywords = random.sample(KEYWORDS, min(15, len(KEYWORDS)))

        print(f"\n[INFO] Searching in subreddits: {daily_subreddits}")
        print(f"[INFO] Using keywords: {daily_keywords}")

        print("\n[INFO] Gathering new authors for the day...")
        daily_authors_pool = gather_potential_authors(
            reddit=search_reddit,
            subreddits=daily_subreddits,
            keywords=daily_keywords,
            limit_per_keyword=LIMIT_PER_KEYWORD,
            already_messaged=already_messaged
        )

        print(f"[INFO] Found {len(daily_authors_pool)} potential authors (not yet messaged).")

        if not daily_authors_pool:
            print("[INFO] No new authors found. Sleeping 12 hours...")
            time.sleep(12 * 3600)
            continue

        random.shuffle(daily_authors_pool)

        chunked_authors = []
        start_index = 0
        for _ in ACCOUNTS:
            end_index = start_index + DAILY_SEND_LIMIT
            chunk = daily_authors_pool[start_index:end_index]
            chunked_authors.append(chunk)
            start_index = end_index

        for i, account in enumerate(ACCOUNTS):
            account_authors = chunked_authors[i]

            if not account_authors:
                print(f"[{account['username']}] No authors available to message.")
                continue

            print(f"\n[INFO] Sending messages for {account['username']}...")
            send_daily_messages_for_account(
                account=account,
                daily_authors=account_authors,
                already_messaged=already_messaged
            )

        print("[INFO] Daily messaging cycle completed. Sleeping 12 hours until next cycle...")
        time.sleep(12 * 3600)  # Sleep 12 hours to optimize API usage


if __name__ == "__main__":
    main()
