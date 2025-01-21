from helpers import *;
from configurations import *;
from creds import *;
from sender import *;
import praw;
import time;
import random


def main():
    already_messaged = load_messaged_authors()

    while True:
        # For each day/cycle: gather potential authors *once*, then distribute them among accounts
        # to minimize repeated searching.

        # You can just gather a large pool once per day using the *first* account's credentials
        # (any account credentials will do for searching).
        # Or you can pick one arbitrarily. We'll pick the first:
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

        # If the pool is empty, just wait 24 hours and try again tomorrow
        if not daily_authors_pool:
            print("[INFO] No new authors found. Sleeping 24 hours...")
            time.sleep(24 * 3600)
            continue

        # We will *split* the daily_authors_pool among the 5 accounts, so each can get up to
        # some portion of the pool (it doesn't have to be even). 
        # We just chunk or slice up daily_authors_pool.  
        # If each account only needs 5 messages, each account only needs ~5 (or more) from that pool.

        # Let's gather at most 5*N accounts. We'll just shuffle the entire pool, then chunk it.

        random.shuffle(daily_authors_pool)
        
        # Each account can get as many authors as it needs. We'll do a simple slice.
        # Alternatively, you could just pass the entire pool to each account; it will only
        # send 5 messages anyway. But let's slice to reduce overhead.
        # (If daily_authors_pool is smaller than needed, accounts won't all get 5.)
        
        chunked_authors = []
        start_index = 0
        for _ in ACCOUNTS:
            end_index = start_index + DAILY_SEND_LIMIT
            chunk = daily_authors_pool[start_index:end_index]
            chunked_authors.append(chunk)
            start_index = end_index

        # Now send messages for each account sequentially
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

        # Once all accounts have sent their daily limit, we sleep until the next cycle.
        # This is a simple approach: we just do it once a day. 
        # Because sequentially sending 25 messages (5 per account) each separated by 1 hour 
        # may actually take ~25 hours total, you might "drift" a bit. 
        # You can refine the timing logic if desired.

        print("[INFO] Daily messaging cycle completed. Sleeping 24 hours until next day...")
        time.sleep(24 * 3600)  # Sleep 24 hours, then repeat


if __name__ == "__main__":
    main()