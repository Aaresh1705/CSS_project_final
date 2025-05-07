import requests
from bs4 import BeautifulSoup
import re

WIKI_API_URL = "https://da.wikipedia.org/w/api.php"


# Infobox (web scraping)

def get_genre_from_infobox(page_id):
    """Fetches the 'genre' field from the infobox of a Wikipedia article by page ID."""
    params = {
        "action": "parse",
        "pageid": page_id,
        "prop": "text",
        "format": "json"
    }
    response = requests.get(WIKI_API_URL, params=params, timeout=20)
    try:
        data = response.json()
    except:
        return "Invalid JSON response"
    
    html_content = data.get("parse", {}).get("text", {}).get("*", "")
    if not html_content:
        return "No content available (infobox)."
    
    soup = BeautifulSoup(html_content, "html.parser")
    infobox = soup.find("table", class_="infobox")
    
    if not infobox:
        return "No infobox found."
    
    for row in infobox.find_all("tr"):
        header = row.find("th")
        if header and "genre" in header.get_text(strip=True).lower():
            genre_td = row.find("td")
            return genre_td.get_text(separator=", ", strip=True) if genre_td else "Genre not found."
    
    return "Genre not found in infobox."


# ---------------------------------------------

# MusicBrainz

MUSICBRAINZ_SEARCH_URL = "https://musicbrainz.org/ws/2/artist/"
MUSICBRAINZ_LOOKUP_URL = "https://musicbrainz.org/ws/2/artist/{mbid}"

def clean_band_name(name):
    return re.sub(r"\s*\(.*?\)", "", name).strip()

def get_title_from_pageid(pageid):
    url = "https://da.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "pageids": pageid,
        "format": "json"
    }
    response = requests.get(url)

    try:
        data = response.json()
    except:
        return "Invalid JSON response"

    
    pages = data.get("query", {}).get("pages", {})
    page = pages.get(str(pageid), {})
    return page.get("title", "Title not found")

def get_musicbrainz_genres(pageid):
    band_name = get_title_from_pageid(pageid)
    cleaned_name = clean_band_name(band_name)

    search_params = {
        "query": f'artist:"{cleaned_name}" AND country:DK',
        "fmt": "json"
    }
    headers = {
        "User-Agent": "GenreFetcher/1.0 (m.brochlips@gmail.com)"  # Replace with your contact
    }

    search_response = requests.get(MUSICBRAINZ_SEARCH_URL, params=search_params, headers=headers)
    if search_response.status_code != 200:
        return f"Search error: {search_response.status_code}"

    artists = search_response.json().get("artists", [])

    for artist in artists:
        if artist.get("type") != "Group":
            continue
        area = artist.get("area", {}).get("name", "")
        if area.lower() != "denmark":
            continue

        mbid = artist.get("id")
        if not mbid:
            continue

        # Step 1: Try with genres only
        lookup_params = {
            "inc": "genres",
            "fmt": "json"
        }
        lookup_response = requests.get(
            MUSICBRAINZ_LOOKUP_URL.format(mbid=mbid),
            params=lookup_params,
            headers=headers,
        )

        if lookup_response.status_code != 200:
            return f"Lookup error: {lookup_response.status_code}"

        
        try:
            artist_data = lookup_response.json()
        except:
            return "Invalid JSON response"

        genres = [g["name"].lower() for g in artist_data.get("genres", [])]

        if genres:
            return ", ".join(sorted(set(genres)))

        # Step 2: Fallback to genres + tags
        fallback_params = {
            "inc": "genres+tags",
            "fmt": "json"
        }
        fallback_response = requests.get(
            MUSICBRAINZ_LOOKUP_URL.format(mbid=mbid),
            params=fallback_params,
            headers=headers,
        )

        if fallback_response.status_code != 200:
            return f"Fallback lookup error: {fallback_response.status_code}"

        try:
            artist_data = fallback_response.json()
        except:
            return "Invalid JSON response"
        
        tags = [t["name"].lower() for t in artist_data.get("tags", [])]
        combined = sorted(set(tags))
        return ", ".join(combined) if combined else "No genres or tags found."

    return "No Danish band found matching that name."


#------------------------------------------------

#NOTE: MASTER FUNCTION 

def get_genre_from_page_id(page_id):
    """Returns the genre(s) of a Wikipedia article (musical group) using Wikidata."""
    
    # Step 1: Get Wikidata ID from page ID
    def get_wikidata_id(page_id):
        params = {
            "action": "query",
            "pageids": page_id,
            "prop": "pageprops",
            "format": "json"
        }
        response = requests.get(WIKI_API_URL, params=params, timeout=20)
        try:
            data = response.json()
        except:
            return "Invalid JSON response"
        pages = data.get("query", {}).get("pages", {})
        page = pages.get(str(page_id), {})
        return page.get("pageprops", {}).get("wikibase_item", None)

    # Step 2: Get genre(s) from Wikidata entity
    def get_genre_from_wikidata(wikidata_id):
        url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"
        response = requests.get(url, timeout=20)
        try:
            data = response.json()
        except:
            return "Invalid JSON response"
        entity = data.get("entities", {}).get(wikidata_id, {})
        claims = entity.get("claims", {})

        genre_ids = [
            claim["mainsnak"]["datavalue"]["value"]["id"]
            for claim in claims.get("P136", [])
            if "mainsnak" in claim and "datavalue" in claim["mainsnak"]
        ]
        
        genres = [get_label_from_wikidata_id(gid) for gid in genre_ids]
        return ", ".join(filter(None, genres)) if genres else "Genre not found."

    # Step 3: Resolve Wikidata entity ID to human-readable label
    def get_label_from_wikidata_id(entity_id):
        url = f"https://www.wikidata.org/wiki/Special:EntityData/{entity_id}.json"

        response = requests.get(url, timeout=20)

        try:
            data = response.json()
        except:
            return "Invalid JSON response"
            
        entity = data.get("entities", {}).get(entity_id, {})
        labels = entity.get("labels", {})
        return labels.get("en", {}).get("value") or labels.get("da", {}).get("value")

    # Combined flow
    wikidata_id = get_wikidata_id(page_id)
    if not wikidata_id:
        out = get_musicbrainz_genres(page_id)
        if isinstance(out, list):
            return out
        else:
            return get_genre_from_infobox(page_id)
        
    return get_genre_from_wikidata(wikidata_id)