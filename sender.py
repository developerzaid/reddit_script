import praw
import time
import random
from configurations import *;
from creds import *;
from helpers import *;


def send_daily_messages_for_account(account, daily_authors, already_messaged):
    """
    Logs into Reddit using 'account' dict credentials.
    Sends up to DAILY_SEND_LIMIT messages to authors from daily_authors (shuffled),
    each separated by 1 hour. Updates global ledger as we go.
    """
    # Create a Reddit instance
    reddit = praw.Reddit(
        client_id=account["client_id"],
        client_secret=account["client_secret"],
        user_agent=account["user_agent"],
        username=account["username"],
        password=account["password"]
    )

    # Shuffle the authors for some randomness
    random.shuffle(daily_authors)

    messages_sent = 0
    for author in daily_authors:
        if messages_sent >= DAILY_SEND_LIMIT:
            break

        try:
            # Choose a random keyword to personalize the message
            chosen_keyword = random.choice(KEYWORDS)
            message_body = MESSAGE_TEMPLATE.format(keyword=chosen_keyword)

            print(f"[{account['username']}] Sending message #{messages_sent+1} to {author}...")
            reddit.redditor(author).message(MESSAGE_SUBJECT, message_body)

            # Update ledger
            already_messaged.add(author)
            add_author_to_ledger(author)

            messages_sent += 1

            # Wait 1 hour (or whatever you set) before sending the next message
            if messages_sent < DAILY_SEND_LIMIT:
                print(f"[{account['username']}] Waiting {DELAY_BETWEEN_MESSAGES} seconds (1 hr) before next message...")
                time.sleep(DELAY_BETWEEN_MESSAGES)

        except Exception as e:
            print(f"[{account['username']}] Failed to send message to {author}: {e}")

    print(f"[{account['username']}] Done. Sent {messages_sent} messages.\n")
