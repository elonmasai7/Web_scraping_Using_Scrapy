# Scrapy settings for buyrentkenya project

BOT_NAME = "buyrentkenya"

SPIDER_MODULES = ["buyrentkenya.spiders"]
NEWSPIDER_MODULE = "buyrentkenya.spiders"

# ----------------------------------------
# Crawler Identification and Behavior
# ----------------------------------------

#USER_AGENT = "buyrentkenya (+http://www.yourdomain.com)"
ROBOTSTXT_OBEY = True

# ----------------------------------------
# Request Configuration
# ----------------------------------------

#DOWNLOAD_DELAY = 3
#CONCURRENT_REQUESTS = 32
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies if not needed
#COOKIES_ENABLED = False

# ----------------------------------------
# AutoThrottle Configuration
# ----------------------------------------

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Initial download delay
AUTOTHROTTLE_MAX_DELAY = 10   # Maximum delay in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Average number of parallel requests
AUTOTHROTTLE_DEBUG = False  # Set to True to show throttling stats

# ----------------------------------------
# Middleware Settings
# ----------------------------------------

DOWNLOADER_MIDDLEWARES = {
    'myproject.middlewares.RotateUserAgentMiddleware': 400,
    'myproject.middlewares.ProxyMiddleware': 410,
    # "buyrentkenya.middlewares.BuyrentkenyaDownloaderMiddleware": 543,  # Uncomment if needed
}

# ----------------------------------------
# scrapy-redis Configuration for Distributed Crawling
# ----------------------------------------

DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# ----------------------------------------
# Item Pipelines
# ----------------------------------------

ITEM_PIPELINES = {
    'myproject.pipelines.MongoDBPipeline': 300,
}

# MongoDB Connection Details
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'scrapy_db'

# ----------------------------------------
# HTTP Cache (optional)
# ----------------------------------------

#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# ----------------------------------------
# Additional Settings
# ----------------------------------------

# Set future-proof default values
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
