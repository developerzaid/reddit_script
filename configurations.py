# configurations.py

# Subreddits to scan (the fixed 5 you want)
SUBREDDITS = ["smallbusiness", "EntrepreneurRideAlong", "entrepreneur", "startups", "Business"]

# Keywords to look for in titles
KEYWORDS = ["New Business", "Business", "startup", "Accounting", "Tech Support", "website development"]

# How many posts to fetch per keyword per subreddit
LIMIT_PER_KEYWORD = 2

# How many messages to send *per account* per day
DAILY_SEND_LIMIT = 5

# Subject line for the private (old-style) message
MESSAGE_SUBJECT = "Hi, Saw your post in a business-related subreddit"

# A simple message template (old PM).
MESSAGE_TEMPLATE = """\
Hey, I saw your post on the subreddit and wondering if you 
need any help with website, Seo or graphics desining. 

I am a freelancer from the UK with 6+ years of experience, and
looking for people who might need help with these services.

If there's something we can collaborate on, would love to get
in touch with you. Here's my email (michael@hazyaztechnologies.com) 
and phone no. (+447466724320)
"""

# Delay between *any* two messages (in seconds) to avoid spamming
# For example, 3600 = 1 hour. You set it to 60s in your snippet:
DELAY_BETWEEN_MESSAGES = 60

# File to store the global ledger of authors already messaged
LEDGER_FILE = "messaged_authors.txt"
