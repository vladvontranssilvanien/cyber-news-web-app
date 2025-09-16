import requests

NEWSAPI_URL = "https://newsapi.org/v2/everything"

def fetch_news(api_key: str, query: str, page_size: int = 12, sort_by: str = "publishedAt", language: str = "en"):
    """Fetch articles from NewsAPI and normalize fields.

    Returns a tuple (articles, error). If error is not None, articles will be empty.
    """
    if not api_key:
        return [], "Missing NEWSAPI_KEY. Set it in your environment."

    params = {
        "q": query,
        "language": language,
        "pageSize": page_size,
        "sortBy": sort_by,
    }
    headers = {"X-Api-Key": api_key}

    try:
        r = requests.get(NEWSAPI_URL, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        articles = []
        for a in data.get("articles", []):
            articles.append({
                "title": a.get("title") or "Untitled",
                "description": a.get("description") or "",
                "url": a.get("url"),
                "source": (a.get("source") or {}).get("name") or "",
                "publishedAt": a.get("publishedAt") or "",
                "image": a.get("urlToImage"),
            })
        return articles, None
    except requests.RequestException as e:
        return [], f"Request failed: {e}"
    except ValueError:
        return [], "Invalid response from NewsAPI"
