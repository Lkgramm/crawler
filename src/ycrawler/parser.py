from bs4 import BeautifulSoup
from typing import List, Dict

def parse_top_news(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")
    items = []

    for row in soup.select("tr.athing"):
        try:
            news_id = row["id"]
            title_tag = row.select_one("a.storylink") or row.select_one("span.titleline a")
            if not title_tag:
                raise ValueError("No title link found")

            url = title_tag.get("href", "#")
            title = title_tag.get_text(strip=True)

            item = {
                "id": news_id,
                "url": url,
                "title": title,
                "comments_url": f"https://news.ycombinator.com/item?id={news_id}"
            }
            items.append(item)
        except Exception as e:
            print(f"Skipping item due to error: {e}")
            continue

    return items


def parse_comment_links(html: str) -> List[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for comment in soup.select(".comment a"):
        href = comment.get("href")
        if href and href.startswith("http"):
            links.append(href)

    return links
