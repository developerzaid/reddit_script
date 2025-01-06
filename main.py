import praw
import time
import random

def main():
    # === 1. Replace with your own Reddit API credentials ===
    CLIENT_ID = "iO2U-ts6W1Ar23IJj_oYbA"
    CLIENT_SECRET = "t1N_H6N13hIwAVViVi5n8FcyLaz2Sg"
    USER_AGENT = "script:keyword_message_script:v1.0 (by u/Opening_Step_9260)"

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
    subreddit_name = "smallbusiness"
    keywords = ["New Business","Business", "startup", "Accounting", "Tech Support","website Development"]
    
    # We'll fetch fewer posts per keyword to stay safe under rate limits
    limit_per_keyword = 2 
    
    # Maximum number of messages we want to send in this run
    daily_send_limit = 5

    # Subject for all messages
    message_subject = "Hi, Saw your post on small business, Do you need any help on your tech side"

    # === 3. Load authors who have already been messaged (from a file or memory) ===
    # In this case, we're using a file to store the authors.
    try:
        with open("messaged_authors.txt", "r") as f:
            messaged_authors = set(f.read().splitlines())
    except FileNotFoundError:
        messaged_authors = set()

    # === 4. Search for authors across multiple keywords ===
    found_authors = set()
    subreddit = reddit.subreddit(subreddit_name)

    for kw in keywords:
        print(f"\nSearching for keyword: '{kw}' (up to {limit_per_keyword} posts)...")
        search_count = 0

        for submission in subreddit.search(kw, sort="top", limit=limit_per_keyword):
            if submission.author and str(submission.author) not in messaged_authors:
                found_authors.add(str(submission.author))
            search_count += 1

        print(f"  -> Collected {search_count} posts for keyword '{kw}'")

    # Convert to a list so we can iterate (or shuffle if desired)
    found_authors_list = list(found_authors)
    random.shuffle(found_authors_list)  # Optional: randomize the order

    print(f"\nTotal unique authors found: {len(found_authors_list)}")

    # === 5. Send messages with a limit and random delay ===
    messages_sent = 0

    for author_name in found_authors_list:
        if messages_sent >= daily_send_limit:
            # We've hit our target of 5 messages for the day
            print(f"\nReached daily send limit of {daily_send_limit} messages. Stopping now.")
            break

        # Example: personalizing the message with a random keyword
        chosen_keyword = random.choice(keywords)
        message_body = (
            f"""  
                Hey! 👋

Hey, I saw your post about {chosen_keyword} and just wanted to say hi! 👋

I am Michael from Hazyaz Technologies. We are great at helping businesses level up their tech game with:
\n\n
Website Development: Building awesome websites\n
SEO: Boosting visibility with SEO\n
Tech Support: Providing solid tech support\n
Graphics Designing : Providing monthly packages for unlimited graphics work\n
If you need any help with this, feel free to reach out! 🙌\n\n

📱 WhatsApp: +44 7466724320
🌐 Website: hazyaztechnologies.com\n\n

No pressure, just here if you need a hand. 😊\n

Cheers,

            """
        )

        try:
            print(f"Sending message #{messages_sent+1} to u/{author_name}...")
            reddit.redditor(author_name).message(subject=message_subject, message=message_body)
            messages_sent += 1

            # Add the author to the messaged list and save it to a file
            messaged_authors.add(author_name)
            with open("messaged_authors.txt", "a") as f:
                f.write(f"{author_name}\n")
        except Exception as e:
            print(f"  -> Failed to send message to {author_name}. Error: {e}")

        # Wait with random delay before sending the next message
        delay_seconds = random.randint(1800, 7200)
        print(f"  -> Waiting {delay_seconds // 60} minutes before sending the next message...")
        time.sleep(delay_seconds)

    print(f"\nAll done! Sent {messages_sent} messages in total.")

if __name__ == "__main__":
    main()
