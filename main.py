import praw
import time
import random
from helpers import *
from configurations import INDUSTRY_SUBREDDITS, KEYWORDS, LIMIT_PER_KEYWORD
from creds import *
from sender import send_daily_messages_for_account, send_followups

def main():
    already_messaged = load_messaged_authors()

    while True:
        # ✅ Randomly select an account for searching Reddit (log in every iteration)
        search_account = random.choice(ACCOUNTS)
        search_reddit = praw.Reddit(
            client_id=search_account["client_id"],
            client_secret=search_account["client_secret"],
            user_agent=search_account["user_agent"],
            username=search_account["username"],
            password=search_account["password"]
        )

        print(f"\n[INFO] Logged in as {search_account['username']} for searching.")

        # ✅ Select 10 random subreddits & 15 random keywords daily
        all_subreddits = [sub for subs in INDUSTRY_SUBREDDITS.values() for sub in subs]  # Flatten dict to list
        daily_subreddits = random.choices(all_subreddits, k=min(10, len(all_subreddits)))  
        daily_keywords = random.choices(KEYWORDS, k=min(15, len(KEYWORDS)))  

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

        # ✅ Distribute authors evenly across accounts
        chunked_authors = [daily_authors_pool[i::len(ACCOUNTS)] for i in range(len(ACCOUNTS))]

        for i, account in enumerate(ACCOUNTS):
            account_authors = chunked_authors[i][:random.randint(3, 5)]  

            if not account_authors:
                print(f"[{account['username']}] No authors available to message.")
                continue

            print(f"\n[INFO] Sending messages for {account['username']}...")
            send_daily_messages_for_account(account, account_authors, already_messaged)

            send_followups(account, already_messaged)

        print("[INFO] Daily messaging cycle completed. Sleeping 12 hours until next cycle...")
        time.sleep(12 * 3600)  # Sleep 12 hours to optimize API usage


if __name__ == "__main__":
    main()
