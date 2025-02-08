import praw
import time
import random
from configurations import *;
from creds import *;
from helpers import *;
from helpers import save_messaged_authors
from configurations import MESSAGE_SUBJECT, MESSAGE_TEMPLATES, DELAY_BETWEEN_MESSAGES


def send_message(reddit, recipient):
    """ Send a direct message to a Reddit user with a random template. """
    try:
        # Randomly select a message template
        message_template = random.choice(MESSAGE_TEMPLATES)
        reddit.redditor(recipient).message(MESSAGE_SUBJECT, message_template)
        print(f"✅ Message sent to u/{recipient}")
        return True
    except Exception as e:
        print(f"⚠️ Failed to send message to u/{recipient}: {e}")
        return False


def send_daily_messages_for_account(account, daily_authors, already_messaged):
    """ Send messages using the given Reddit account. """
    reddit = praw.Reddit(
        client_id=account["client_id"],
        client_secret=account["client_secret"],
        user_agent=account["user_agent"],
        username=account["username"],
        password=account["password"]
    )

    sent_count = 0

    for author in daily_authors:
        if author in already_messaged:
            print(f"⏩ Skipping u/{author} (Already messaged)")
            continue

        success = send_message(reddit, author)

        if success:
            already_messaged.add(author)
            sent_count += 1

        if sent_count >= 5:  # Limit per account per day
            print(f"🚀 {account['username']} reached the daily limit.")
            break

        print(f"⏳ Waiting {DELAY_BETWEEN_MESSAGES / 60} min before next message...")
        time.sleep(DELAY_BETWEEN_MESSAGES)

    save_messaged_authors(already_messaged)
