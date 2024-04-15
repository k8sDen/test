import logging
from concurrent.futures import as_completed, ThreadPoolExecutor
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from parser.models import Post

from app.celery import app

logger = logging.getLogger('app')


def load_url(url):
    response = requests.get(url)
    return response.text


def download_sites(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                soup = BeautifulSoup(data, 'html.parser')
                news_items = soup.find_all('div', {"class": "article_mainpage"})
                posts = []
                for item in news_items:
                    link = f"https://afk.kz{item.find_all('a')[0].get('href')}"
                    title = item.find_all("div", {"class": "article_title"})[0].text.strip()
                    published_at = item.find_all("div", {"class": "published_at"})[0].text.strip()
                    posts.append(Post(title=title, link=link, published_at=datetime.strptime(published_at, '%d.%m.%Y')))
                if len(posts) > 0:
                    Post.objects.bulk_create(posts, 100)
                    logger.info(f"Успешно получено {len(posts)} новости.")
            except Exception as exc:
                print(f'{url} сгенерировал исключение: {str(exc)}')


@app.task
def fetch_news_from_afk():
    urls = [
        "https://afk.kz/ru/news/?page=1&cultureKey=ru",
        "https://afk.kz/ru/news/?page=2&cultureKey=ru",
        "https://afk.kz/ru/news/?page=3&cultureKey=ru",
        "https://afk.kz/ru/news/?page=4&cultureKey=ru",
        "https://afk.kz/ru/news/?page=5&cultureKey=ru",
    ]
    download_sites(urls)
