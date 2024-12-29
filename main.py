import praw
import time

def main():
    # === 1. Replace with your own Reddit API credentials ===
    CLIENT_ID = "iO2U-ts6W1Ar23IJj_oYbA"
    CLIENT_SECRET = "t1N_H6N13hIwAVViVi5n8FcyLaz2Sg"
    USER_AGENT = "script:keyword_message_script:v1.0 (by u/Opening_Step_9260)"

    # If you want to send messages, you need a username and password login:
    REDDIT_USERNAME = "Opening_Step_9260"
    REDDIT_PASSWORD = "Alaska2020$"

    # Create a Reddit instance with username/password for messaging
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD
    )

    # === 2. Define your search parameters ===
    subreddit_name = "test"        # e.g., "AskReddit", "python", etc.
    keyword = "keyword_to_search"  # e.g., "Python", "API", etc.
    limit = 50                     # number of search results to process

    # === 3. Define the content of the message you want to send ===
    message_subject = "Hello from a script!"
    message_body = (
        "Hi there, Can i ask you a question?.\n\n"

    )

    # === 4. Collect authors of top posts matching your keyword ===
    found_authors = []
    subreddit = reddit.subreddit(subreddit_name)

    # Use the subreddit search, sorting by top. 
    # You can add time_filter="week" or "day" if you want more recent top posts.
    for submission in subreddit.search(keyword, sort="top", limit=limit):
        # submission.author may be None if the account is deleted or suspended
        if submission.author and str(submission.author) not in found_authors:
            found_authors.append(str(submission.author))

    print(f"Found {len(found_authors)} unique authors from the top {limit} posts.")

    # === 5. Send messages to each author with a 5-minute delay between messages ===
    for i, author_name in enumerate(found_authors, start=1):
        try:
            print(f"Sending message to {author_name} ({i}/{len(found_authors)})...")
            reddit.redditor(author_name).message(subject=message_subject, message=message_body)
            print("  -> Message sent. Waiting 5 minutes to send the next one...")
        except Exception as e:
            print(f"  -> Failed to send message to {author_name}. Error: {e}")

        # Wait 5 minutes (300 seconds) before sending the next message
        time.sleep(300)  

    print("\nAll done!")

if __name__ == "__main__":
    main()
