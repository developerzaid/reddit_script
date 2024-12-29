import praw

reddit = praw.Reddit(
    
    client_id = "iO2U-ts6W1Ar23IJj_oYbA",
    client_secret = "t1N_H6N13hIwAVViVi5n8FcyLaz2Sg",
    user_agent = "script:keyword_message_script:v1.0 (by u/Opening_Step_9260)",
    username = "Opening_Step_9260",
    password = "Alaska2020$",
)

try:
    recipient = "sazia24"
    subject = "Test Message"
    body = "Hello from a test script!"
    reddit.redditor(recipient).message(subject="Your Subject", message="Your Message Body")
    print("Message sent successfully!")
except Exception as e:
    print("Failed to send message:", e)
