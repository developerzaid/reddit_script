# helpers.py

from configurations import LEDGER_FILE

def add_author_to_ledger(author_name):
    """Append an author's username to the ledger file."""
    with open(LEDGER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{author_name}\n")

def load_messaged_authors():
    """
    Load a set of authors from the ledger file,
    so we don't message them again.
    """
    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()
