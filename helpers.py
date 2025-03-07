import json
import time
from configurations import LEDGER_FILE

def gather_potential_authors(reddit, subreddits, keywords, limit_per_keyword, already_messaged):
    """Search for potential authors based on random subreddits & keywords."""
    authors = set()

    for subreddit in subreddits:
        for keyword in keywords:
            print(f"🔍 Searching '{keyword}' in r/{subreddit}...")

            try:
                search_results = reddit.subreddit(subreddit).search(keyword, limit=limit_per_keyword)

                for post in search_results:
                    author = post.author.name if post.author else None
                    if author and author not in already_messaged:
                        authors.add((author, subreddit, keyword))

            except Exception as e:
                print(f"⚠️ Error searching in r/{subreddit}: {e}")

    return list(authors)  # ✅ Convert to list before returning (avoids duplicates)

