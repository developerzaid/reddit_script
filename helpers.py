import json
import os
from configurations import LEDGER_FILE

def load_messaged_authors():
    if not os.path.exists(LEDGER_FILE):
        return {}

    with open(LEDGER_FILE, "r") as file:
        return json.load(file)


def save_messaged_authors(authors):
    with open(LEDGER_FILE, "w") as file:
        json.dump(authors, file)


def gather_potential_authors(reddit, subreddits, keywords, limit_per_keyword, already_messaged):
    authors = set()
    for subreddit in subreddits:
        for keyword in keywords:
            try:
                search_results = reddit.subreddit(subreddit).search(keyword, limit=limit_per_keyword)
                for post in search_results:
                    if post.author and post.author.name not in already_messaged:
                        authors.add((post.author.name, subreddit, keyword))
            except Exception as e:
                print(f"⚠️ Error in r/{subreddit} - {e}")

    return list(authors)
