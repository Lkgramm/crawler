import aiohttp
from aiohttp import ClientSession

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; YcrawlerBot/1.0; +https://news.ycombinator.com/)"
}

async def fetch_url(session: ClientSession, url: str) -> str:
    try:
        async with session.get(url, headers=HEADERS, timeout=15) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""