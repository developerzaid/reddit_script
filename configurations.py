# Subreddits to scan (the fixed 5 you want)
SUBREDDITS = ["smallbusiness", "EntrepreneurRideAlong", "entrepreneur", "startups", "Business"]  

# Keywords to look for in titles
KEYWORDS = ["New Business", "Business", "startup", "Accounting", "Tech Support", "website development"]

# How many posts to fetch per keyword per subreddit
LIMIT_PER_KEYWORD = 2

# How many messages to send *per account* per day
DAILY_SEND_LIMIT = 5

# Subject line for the private message
MESSAGE_SUBJECT = "Hi, Saw your post in a business-related subreddit"

# A simple message template (you can further personalize it if you wish)
# You can include placeholders for random keywords, etc.
MESSAGE_TEMPLATE = """\
Hey, I saw your post on the subreddit and wondering if you 
need any help with website, Seo or graphics desining. 

I am freelancer from UK with 6+ years of experince, and
looking for people who might need help with these services.

If there's something we can collaborate on, would love to get
in touch with you. here's my email(michael@hazyaztechnologies.com) 
and phone no (+447466724320)
"""

# Delay between *any* two messages to avoid spamming (in seconds)
# 1 hour = 3600 seconds
DELAY_BETWEEN_MESSAGES = 60  

# File to store the global ledger of authors already messaged
LEDGER_FILE = "messaged_authors.txt"
