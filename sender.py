import praw
import random
import time
from configurations import INDUSTRY_SUBREDDITS, INDUSTRY_MESSAGES, MESSAGE_TEMPLATES, MESSAGE_SUBJECT, FOLLOWUP_MESSAGES
from helpers import save_messaged_authors

def send_message(reddit, recipient, subreddit, keyword, is_followup=False):
    try:
        message = None
        for industry, subs in INDUSTRY_SUBREDDITS.items():
            if subreddit in subs:
                message = INDUSTRY_MESSAGES[industry].format(username=recipient, subreddit=subreddit, keyword=keyword)
                break

        if not message:
            message = random.choice(FOLLOWUP_MESSAGES if is_followup else MESSAGE_TEMPLATES).format(username=recipient, subreddit=subreddit, keyword=keyword)

        reddit.redditor(recipient).message(MESSAGE_SUBJECT.format(subreddit=subreddit), message)
        print(f"✅ {'Follow-up' if is_followup else 'Initial'} message sent to {recipient}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to message {recipient}: {e}")
        return False


def send_followups(account, already_messaged):
    reddit = praw.Reddit(**account)
    to_remove = []

    for author, data in already_messaged.items():
        if time.time() >= data["followup_scheduled"]:
            if send_message(reddit, author, data["subreddit"], data["keyword"], is_followup=True):
                to_remove.append(author)

    for author in to_remove:
        del already_messaged[author]

    save_messaged_authors(already_messaged)
