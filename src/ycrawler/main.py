# src/ycrawler/main.py
import asyncio

from ycrawler.fetcher import fetch_url
from ycrawler.parser import parse_top_news
from ycrawler.storage import save_news_package

ROOT_URL = "https://news.ycombinator.com/"
SEEN_IDS = set()
INTERVAL = 60  # N секунд

async def crawl():
    from aiohttp import ClientSession

    async with ClientSession() as session:
        html = await fetch_url(session, ROOT_URL)
        news_items = parse_top_news(html)

        for item in news_items:
            if item["id"] in SEEN_IDS:
                continue
            SEEN_IDS.add(item["id"])
            await save_news_package(session, item)

async def main():
    while True:
        try:
            await crawl()
        except Exception as e:
            print(f"Error during crawl: {e}")
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
