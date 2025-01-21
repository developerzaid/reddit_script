from configurations import *;

def add_author_to_ledger(author_name):
    """Append an author's username to the ledger file."""
    with open(LEDGER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{author_name}\n")


# ─────────────────────────────────────────────────────────────────────────────
# 5. Gather authors from all subreddits & keywords (one search pass per day)
# ─────────────────────────────────────────────────────────────────────────────
def gather_potential_authors(reddit, subreddits, keywords, limit_per_keyword, already_messaged):
    """
    Perform searches on the specified subreddits, using the given keywords.
    Returns a list of authors (usernames as strings) who have NOT been messaged yet.
    """
    found_authors = set()

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)

        for kw in keywords:
            # We use the .search() method with a small limit to avoid heavy API usage
            for submission in subreddit.search(kw, sort="new", limit=limit_per_keyword):
                if submission.author is None:
                    continue

                author_str = str(submission.author).lower()
                # Only add if not already messaged
                if author_str not in already_messaged:
                    found_authors.add(author_str)

    return list(found_authors)

def load_messaged_authors():
    try:
        with open("messaged_authors.txt", "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()