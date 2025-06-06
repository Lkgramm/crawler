import os
from typing import Dict, List
import aiofiles
from aiohttp import ClientSession

from ycrawler.fetcher import fetch_url
from ycrawler.parser import parse_comment_links

BASE_DIR = "data"

async def save_page(folder: str, name: str, content: str):
    path = os.path.join(BASE_DIR, folder)
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, f"{name}.html")
    async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
        await f.write(content)

async def save_news_package(session: ClientSession, item: Dict):
    news_id = item["id"]
    title = item["title"]
    url = item["url"]
    comments_url = item["comments_url"]

    # 1. Сохраняем основную страницу новости
    news_html = await fetch_url(session, url)
    await save_page(news_id, "main", news_html)

    # 2. Сохраняем страницу с комментариями
    comments_html = await fetch_url(session, comments_url)
    await save_page(news_id, "comments", comments_html)

    # 3. Извлекаем ссылки из комментариев и сохраняем их
    comment_links = parse_comment_links(comments_html)
    for i, link in enumerate(comment_links):
        page_html = await fetch_url(session, link)
        if page_html:
            await save_page(news_id, f"comment_{i}", page_html)

    print(f"Saved news {news_id}: {title}")
