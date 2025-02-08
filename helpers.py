from configurations import *;


def gather_potential_authors(reddit, subreddits, keywords, limit_per_keyword, already_messaged):
    """ Search for potential authors based on random subreddits & keywords. """
    authors = set()

    for subreddit in subreddits:
        for keyword in keywords:
            print(f"🔍 Searching '{keyword}' in r/{subreddit}...")

            try:
                search_results = reddit.subreddit(subreddit).search(keyword, limit=limit_per_keyword)

                for post in search_results:
                    author = post.author.name if post.author else None

                    if author and author not in already_messaged:
                        authors.add(author)

            except Exception as e:
                print(f"⚠️ Error searching in r/{subreddit}: {e}")

    return list(authors)


def load_messaged_authors():
    """ Load already messaged authors from file to avoid duplicates. """
    try:
        with open("messaged_authors.txt", "r") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()


def save_messaged_authors(already_messaged):
    """ Save messaged authors to prevent duplicate messaging. """
    with open("messaged_authors.txt", "w") as file:
        for author in already_messaged:
            file.write(author + "\n")
