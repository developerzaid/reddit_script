import praw
import time
import random
from helpers import gather_potential_authors, load_messaged_authors, save_messaged_authors
from configurations import INDUSTRY_SUBREDDITS, KEYWORDS, LIMIT_PER_KEYWORD
from creds import ACCOUNTS
from sender import send_message, send_followups

def main():
    already_messaged = load_messaged_authors()

    while True:
        # ✅ Randomly select Reddit account for searching
        search_account = random.choice(ACCOUNTS)
        search_reddit = praw.Reddit(
            client_id=search_account["client_id"],
            client_secret=search_account["client_secret"],
            user_agent=search_account["user_agent"],
            username=search_account["username"],
            password=search_account["password"]
        )

        print(f"[INFO] Logged in as {search_account['username']} for searching.")

        # ✅ Daily Random Subreddits & Keywords
        all_subreddits = [sub for subs in INDUSTRY_SUBREDDITS.values() for sub in subs]
        daily_subreddits = random.sample(all_subreddits, min(10, len(all_subreddits)))
        daily_keywords = random.sample(KEYWORDS, min(15, len(KEYWORDS)))

        print(f"[INFO] Searching in: {daily_subreddits}")
        print(f"[INFO] Keywords: {daily_keywords}")

        # 🔍 Gather Potential Authors
        daily_authors = gather_potential_authors(search_reddit, daily_subreddits, daily_keywords, LIMIT_PER_KEYWORD, already_messaged)
        print(f"[INFO] Found {len(daily_authors)} new authors.")

        if not daily_authors:
            print("[INFO] No new authors. Sleeping 12 hours...")
            time.sleep(12 * 3600)
            continue

        random.shuffle(daily_authors)

        # ✅ Split authors across accounts
        chunked_authors = [daily_authors[i::len(ACCOUNTS)] for i in range(len(ACCOUNTS))]

        for i, account in enumerate(ACCOUNTS):
            if not chunked_authors[i]:
                print(f"[{account['username']}] No authors to message.")
                continue

            reddit = praw.Reddit(**account)
            for author, subreddit, keyword in chunked_authors[i][:random.randint(3, 5)]:
                if send_message(reddit, author, subreddit, keyword):
                    already_messaged[author] = {
                        "subreddit": subreddit,
                        "keyword": keyword,
                        "followup_scheduled": time.time() + random.randint(172800, 345600)
                    }
                    save_messaged_authors(already_messaged)

            send_followups(account, already_messaged)

        print("[INFO] Cycle completed. Sleeping 12 hours...")
        time.sleep(12 * 3600)


if __name__ == "__main__":
    main()
