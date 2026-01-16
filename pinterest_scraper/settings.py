import os # ضروري لقراءة المتغيرات من Railway

BOT_NAME = 'pinterest_scraper'

SPIDER_MODULES = ['pinterest_scraper.spiders']
NEWSPIDER_MODULE = 'pinterest_scraper.spiders'

# عدم الانصياع لملف robots.txt للسماح بالكشط
ROBOTSTXT_OBEY = False

# --- إعدادات ScrapeOps الذكية ---
# سيقوم الكود بالبحث عن متغير اسمه SCRAPEOPS_API_KEY في إعدادات Railway
SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY', 'ضع_مفتاحك_هنا_في_حال_التجربة_المحلية')
SCRAPEOPS_PROXY_ENABLED = True
SCRAPEOPS_MONITOR_ENABLED = True

# --- تفعيل الـ Middlewares (مهم جداً للبروكسي) ---
DOWNLOADER_MIDDLEWARES = {
    # تنشيط البروكسي الخاص بـ ScrapeOps لتجنب الحظر
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    # إضافة نظام إعادة المحاولة التلقائي في حال فشل الطلب
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}

# إعدادات الأداء (لعدم الضغط على السيرفر وضمان الاستمرارية)
CONCURRENT_REQUESTS = 5 # يمكن رفعها قليلاً لأننا نستخدم بروكسي
DOWNLOAD_DELAY = 0.5 

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# ربط نظام استخراج البيانات
ITEM_PIPELINES = {
   'pinterest_scraper.pipelines.PinterestScrapyPipeline': 300,
}

# التحجيم التلقائي لسرعة الكشط
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# توافق النسخ المستقبلية
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
