from fastapi import FastAPI, BackgroundTasks
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Pinterest Scraper API is running!"}

@app.get("/scrape")
def run_scraper(query: str, background_tasks: BackgroundTasks):
    # وظيفة لتشغيل الكشط في الخلفية حتى لا ينتظر n8n طويلاً
    def start_scraping(search_query):
        command = f"scrapy crawl pinterest_search -a search_query='{search_query}'"
        subprocess.run(command, shell=True)

    background_tasks.add_task(start_scraping, query)
    return {"status": "Scraping started", "query": query}
