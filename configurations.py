# Subreddits to scan (the fixed 5 you want)
SUBREDDITS = ["smallbusiness", "EntrepreneurRideAlong", "entrepreneur", "startups", "Business" , 
              "smallbusinessuk", "SmallBusinessCanada", "smallbusinesssupport", "SmallBusinessSellers", 
              "small_business_ideas", "smallbusinessUS", "Business_Ideas", "Entrepreneur", "Entrepreneurship", 
              "growmybusiness", "advancedentrepreneur", "indiebiz", "RealEstate", "askuk","casualuk",
              "realestateinvesting", "Landlord", "AirBnBInvesting", "realtors", "Dentistry", 
              "healthcare", "RealEstateAdvice", "Fitness", "yoga", "pilates", "sidehustle", "sidehustle_ideas", "sidehustles"]  

# Keywords to look for in titles
KEYWORDS = ["New Business", "Business", "startup", "Tech Support", "website development", "web development", "web design", 
            "online business", "ecommerce", "starting business", "online selling", "website redesign", "graphics designer", 
            "need a logo", "task", "building website", "digital marketing", "SEO", "search engine optimization", "local SEO", 
            "on-page SEO", "off-page SEO", "SEO audit", "responsive design", "mobile website design", "professional website design", 
            "UI design", "UX design", "branding", "brand identity", "logo design service", "graphic design", "creative design", 
            "eCommerce website design", "WordPress website design", "custom website design", "CMS development", "small business website", 
            "business website design", "modern website design", "website optimization", "website speed", "affordable website design", 
            "startup website", "SEO copywriting", "content marketing", "digital strategy", "online presence", "creative agency", 
            "digital design", "visual identity", "social media graphics", "website maintenance", "hire web developer", 
            "hire graphic designer", "affordable SEO services", "professional SEO", "Google ranking", "organic search", 
            "keyword research", "digital presence"]


# How many posts to fetch per keyword per subreddit
LIMIT_PER_KEYWORD = 1

# How many messages to send *per account* per day
DAILY_SEND_LIMIT = 5

# Subject line for the private message
MESSAGE_SUBJECT = "Hi, Saw your post in a subreddit"

# A simple message template (you can further personalize it if you wish)
# You can include placeholders for random keywords, etc.

MESSAGE_TEMPLATES = [
    """Hey, I saw your post on the subreddit and wondering if you 
    need any help with website, Seo or graphics desining. 

    I am freelancer from UK with 6+ years of experince, and
    looking for people who might need help with these services.

    If there's something we can work on, would love to get
    in touch with you. here's my email(michael@hazyaztechnologies.com)""",

    """Hey! I saw your post and just wanted to check in,
    Are you currently looking for help with your website, SEO, or graphics design?

    I run a small agency here in the UK, and we have been helping businesses with this for over 6 years. 
    If you ever want to chat or need some support, feel free to reach out! 

    You can email me at michael@hazyaztechnologies.com or just reply""",

    """Hey..! Wassup? I saw your post on the 
    subreddit and was wondering if you need any help with website or SEO?

    Im a freelancer based in UK with 6+ years of experience in website development
    and if you need any help with it i would love to get in touch with you.

    You can email me(Michael@hazyaztechnologies.com) or just reply on this."""
]
# Delay between *any* two messages to avoid spamming (in seconds)
# 1 hour = 3600 seconds
DELAY_BETWEEN_MESSAGES = 1800  

# File to store the global ledger of authors already messaged
LEDGER_FILE = "messaged_authors.txt"
