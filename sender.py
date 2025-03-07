import praw
import time
import random
from configurations import *
from helpers import *

def send_message(reddit, recipient, subreddit, keyword, is_followup=False):
    """Send a personalized message based on subreddit or keyword."""
    try:
        selected_message = None
        for industry, subs in INDUSTRY_SUBREDDITS.items():
            if subreddit in subs:
                selected_message = INDUSTRY_MESSAGES[industry].format(username=recipient, subreddit=subreddit, keyword=keyword)
                break

        if not selected_message:
            selected_message = (random.choice(FOLLOWUP_MESSAGES) if is_followup else random.choice(MESSAGE_TEMPLATES)).format(username=recipient, subreddit=subreddit, keyword=keyword)

        reddit.redditor(recipient).message(MESSAGE_SUBJECT, selected_message)
        print(f"✅ {'Follow-up' if is_followup else 'Initial'} message sent to u/{recipient} (r/{subreddit}, keyword: {keyword})")
        return True

    except Exception as e:
        print(f"⚠️ Failed to send message to u/{recipient}: {e}")
        return False


def send_followups(account, already_messaged):
    """Send follow-up messages after the delay."""
    reddit = praw.Reddit(**account)

    to_remove = []  # ✅ Store users to remove to avoid modifying dict while iterating

    for author, data in already_messaged.items():
        if time.time() >= data.get("followup_scheduled", float('inf')):
            if send_message(reddit, author, data["subreddit"], data["keyword"], is_followup=True):
                to_remove.append(author)

    for author in to_remove:
        del already_messaged[author]  # ✅ Safely remove users

    save_messaged_authors(already_messaged)
