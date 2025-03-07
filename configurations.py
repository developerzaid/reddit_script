import random

# 🚀 Industry-specific subreddits
INDUSTRY_SUBREDDITS = {
    "real_estate": ["realestateinvesting", "Landlord", "realtors", "AirBnBInvesting", "RealEstate", "RealEstateAdvice"],
    "plumbing": ["Plumbing", "Plumbingpros"],
    "electricians": ["electricians", "electrical"],
    "finance": ["accounting", "financialindependence", "personalfinance"],
    "construction": ["Construction", "Contractor"],
    "healthcare": ["healthcare", "Dentistry"],
    "fitness": ["PersonalTraining", "Fitness", "yoga", "pilates"],
    "tech": ["webdev", "SEO", "SmallBusinessIT"],
    "business": ["smallbusiness",  "Business",
                         "smallbusinessuk", "SmallBusinessCanada", "smallbusinesssupport", "SmallBusinessSellers",
                         "small_business_ideas", "smallbusinessUS"],
    "side_hustles": ["sidehustle", "sidehustle_ideas", "sidehustles"],
    "other": ["askuk","EntrepreneurRideAlong", "entrepreneur", "startups","Business_Ideas", "Entrepreneur", "Entrepreneurship",
                         "growmybusiness", "advancedentrepreneur", "indiebiz"],
 # Subreddits that don't fit into any industry
}

# 💬 Industry-specific messages
INDUSTRY_MESSAGES = {
    "real_estate": "Hey {username}, saw your post in r/{subreddit}! A lot of realtors struggle to stand out online and get consistent buyer/seller leads. I help real estate pros build high-converting websites that showcase their listings and rank on Google for local buyers. How are you currently getting most of your leads?",
    "plumbing": "Hey {username}, noticed your post in r/{subreddit}. I work with plumbers to set up strong online presence—so local customers find you when they need help. Do most of your jobs come from word-of-mouth, or do you have a website bringing in clients?",
    "electricians": "Hey {username}, saw your post in r/{subreddit}. Many electricians struggle with online visibility. I help set up professional websites and local SEO so customers searching for your services find you first. How are you getting most of your work right now?",
    "finance": "Hey {username}, saw your post in r/{subreddit}! Many finance professionals struggle to build trust online. I help create professional websites that build credibility and attract new clients. How are most of your new clients finding you?",
    "construction": "Hey {username}, noticed your post in r/{subreddit}. I help construction businesses get more projects by building strong online credibility. A website that showcases your past projects can bring in more clients. How do you currently attract new customers?",
    "healthcare": "Hey {username}, saw your post in r/{subreddit}. Many healthcare professionals struggle to establish a strong online presence. I help dentists, doctors, and clinics build professional websites that attract more patients. How do you currently bring in new clients?",
    "fitness": "Hey {username}, came across your post in r/{subreddit}. I help fitness trainers and gyms build websites that attract more clients. Are most of your clients coming from social media, or do you have a website bringing in leads?",
    "tech": "Hey {username}, noticed your post in r/{subreddit}. A lot of tech startups and freelancers struggle to stand out. I help create high-quality websites that showcase skills, services, and rank well on Google. How do you currently attract new clients?",
    "entrepreneurship": "Hey {username}, noticed your post in r/{subreddit}. I work with small business owners and entrepreneurs to build strong online credibility through professional websites and SEO. What’s the biggest challenge you’re facing in growing your business?",
    "side_hustles": "Hey {username}, saw your post in r/{subreddit}. Many people struggle to turn their side hustle into a full-time business. I help side hustlers build websites that establish credibility and attract more clients. Where are most of your leads coming from right now?",
    "other": "Hey {username}, saw your post in r/{subreddit}. Just curious—what is been your experience with {keyword} so far?"
}

# 🔄 General message templates (for subreddits that are NOT in the industry list)
MESSAGE_TEMPLATES = [
    "Hey {username}, saw your post in r/{subreddit} about \"{keyword}\"—really interesting! I’ve talked to many people working on this, and everyone takes a different approach. Curious—what’s been working best for you so far?",
    "Hey {username}, noticed your post in r/{subreddit} about \"{keyword}\"—love seeing people dive into this! What’s been your biggest win so far?",
    "Hey {username}, came across your post in r/{subreddit} about \"{keyword}\"—awesome stuff! Everyone faces different challenges with this. What’s been the most surprising thing for you so far?"
]

# 🔄 Follow-up messages
FOLLOWUP_MESSAGES = [
    "Hey {username}, just wanted to check in—how’s everything going with {keyword}? Any updates since we last chatted? Always curious to hear how things progress!",
    "Hey {username}, was thinking about our last chat on {keyword}. Let me know if you ever want to bounce around ideas—I always love hearing what others are working on! No rush, just here if you ever want to chat :)",
    "Hey {username}, just popping back in—did you ever figure out that thing with {keyword}? Would love to hear how it’s going! Hope all’s good on your end :)"
]

# 🔍 Keywords to search for
KEYWORDS = [
    # 🚀 Business Strategy & Growth
    "customer acquisition", "business growth", "small business scaling",
    "marketing strategies", "increasing sales", "business networking",
    "pricing strategies", "business partnerships", "business automation",
    "CRM software", "business stagnation",

    # 💰 Business Finance & Funding
    "small business funding", "business loans", "startup grants",
    "loan advice", "business credit cards", "bootstrapping a business",
    "angel investors", "startup investors", "crowdfunding",
    "business savings",

    # 💼 Business Operations & Management
    "payroll services",
    "business registration", "business planning",
    "small business taxes", "bookkeeping",
    "supplier negotiation", "client management",

    # 🛒 E-commerce & Retail
    "eCommerce platforms", "starting an online store", "POS systems",
    "Etsy vs Shopify vs Amazon", "eCommerce sales growth", "private label",
    "inventory management", "pricing strategy",

    # 📢 Marketing & Branding
    "local marketing", "customer acquisition", "Facebook advertising",
    "Instagram growth", "lead generation", "personal branding",
    "LinkedIn marketing", "email marketing", "website conversion optimization",
    "Google reviews", "influencer marketing",

    # 🏠 Side Hustles & Passive Income
    "side hustle ideas", "starting a side business", "scaling a side hustle",
    "profitable small businesses", "freelancing vs entrepreneurship", "Airbnb business",
    "passive income strategies", "making money online", "rental property business",

]
# 📩 Message subject line
MESSAGE_SUBJECT = "Hey, saw your post in r/{subreddit}!"

# ⏳ Delay between messages (30-60 minutes)
DELAY_BETWEEN_MESSAGES = random.randint(1800, 3600)

# ⏳ Delay for follow-ups (2-4 days)
FOLLOWUP_DELAY = random.randint(172800, 345600)  # 48-96 hours

# 📝 File to store authors who have already been messaged
LEDGER_FILE = "messaged_authors.txt"

# 🔢 Limits
LIMIT_PER_KEYWORD = 1  # How many posts to fetch per keyword per subreddit
DAILY_SEND_LIMIT = 5  # How many messages to send per account per day

# 🔍 Keywords to search for (unchanged)

