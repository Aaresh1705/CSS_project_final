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

