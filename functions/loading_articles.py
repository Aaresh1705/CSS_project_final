import requests


WIKI_API_URL = "https://da.wikipedia.org/w/api.php"


def get_category_members(category, limit=10000, cmcontinue=None):
    """Fetches articles from a given category."""
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": category,
       "cmlimit": limit,
        "cmtype": "page",
        "format": "json"
    }
    
    if cmcontinue:
        params["cmcontinue"] = cmcontinue

    response = requests.get(WIKI_API_URL, params=params)
    return response.json()

def get_music_articles(categories):
    """Fetches Wikipedia articles related to musicians, bands, and music."""
    
    articles = []
    
    for category in categories:
        print(f"Fetching articles from: {category}")
        data = get_category_members(category)
        articles.extend(data.get("query", {}).get("categorymembers", []))
    
    return articles


def get_article_content_by_id(page_id):
    """Fetches the introduction text of a Wikipedia article by page ID."""
    params = {
        "action": "query",
        "prop": "extracts",
        "pageids": page_id,  # Use page ID instead of title
        "exintro": True,     # Only fetch the intro section
        "format": "json"
    }
    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()
    
    pages = data.get("query", {}).get("pages", {})
    page_info = pages.get(str(page_id), {})
    return page_info.get("extract", "No content available.")