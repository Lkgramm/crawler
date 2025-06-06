# Ycrawler — Асинхронный краулер для Hacker News

**Ycrawler** — асинхронный краулер, который каждые N секунд обходит топ-30 новостей на [news.ycombinator.com](https://news.ycombinator.com), скачивает саму новость, страницу комментариев и все внешние ссылки из комментариев.

---

## 🛠 Установка

```bash
git clone https://github.com/your_username/ycrawler.git
cd ycrawler
poetry install
````

---

## ▶️ Запуск

```bash
make run
```

По умолчанию интервал между итерациями — 60 секунд. Его можно изменить в файле `src/ycrawler/main.py`:

```python
INTERVAL = 60  # в секундах
```

---

## 💬 Пример вывода

```bash
$ make run
poetry run python src/ycrawler/main.py
Failed to fetch https://addons.thunderbird.net/en-US/thunderbird/addon/removedupes/: 403, message='Forbidden', url='https://addons.thunderbird.net/en-US/thunderbird/addon/removedupes/'
Saved news 44201975: How we decreased GitLab repo backup times from 48 hours to 41 minutes
Saved news 44204224: A year of funded FreeBSD development
Failed to fetch https://cointelegraph.com/news/neuromorphic-computing-breakthrough-enable-blockchain-mars: 403, message='Forbidden', url='https://cointelegraph.com/news/neuromorphic-computing-breakthrough-enable-blockchain-mars'
Saved news 44201812: Sandia turns on brain-like storage-free supercomputer
Saved news 44204277: United States Digital Service Origins
Saved news 44200866: Odyc.js – A tiny JavaScript library for narrative games
Saved news 44204928: Onyx (YC W24) – AI Assistants for Work Hiring Founding AE
Saved news 44204181: Show HN: AI game animation sprite generator
```

---

## 📦 Зависимости

* Python 3.13
* aiohttp
* aiofiles
* beautifulsoup4

Устанавливаются через `poetry install`.

```
