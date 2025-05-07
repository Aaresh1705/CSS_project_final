import numpy as np
import requests
from bs4 import BeautifulSoup


WIKI_API_URL = "https://da.wikipedia.org/w/api.php"
WIKIDATA_API_URL = "https://www.wikidata.org/w/api.php"

def get_wikidata_id(title):
    """Fetches the Wikidata ID of a Wikipedia article."""
    params = {
        "action": "query",
        "titles": title,
        "prop": "pageprops",
        "format": "json"
    }
    response = requests.get(WIKI_API_URL, params=params).json()
    pages = response.get("query", {}).get("pages", {})
    
    for page in pages.values():
        return page.get("pageprops", {}).get("wikibase_item")

def get_members_from_wikidata(wikidata_id):
    """Fetches members of a band from Wikidata."""
    params = {
        "action": "wbgetentities",
        "ids": wikidata_id,
        "props": "claims",
        "format": "json"
    }
    response = requests.get(WIKIDATA_API_URL, params=params).json()
    
    claims = response.get("entities", {}).get(wikidata_id, {}).get("claims", {})
    members = []

    # P527 = has part / member
    if "P527" in claims:
        for part in claims["P527"]:
            try:
                member_id = part["mainsnak"]["datavalue"]["value"]["id"]
                member_name = get_label_from_wikidata(member_id)
                members.append(member_name)
            except KeyError:
                continue

    return members

def get_label_from_wikidata(entity_id):
    """Fetches the label (name) of a Wikidata entity."""
    params = {
        "action": "wbgetentities",
        "ids": entity_id,
        "props": "labels",
        "languages": "da",  # Danish labels
        "format": "json"
    }
    response = requests.get(WIKIDATA_API_URL, params=params).json()
    return response.get("entities", {}).get(entity_id, {}).get("labels", {}).get("da", {}).get("value", "Unknown")

def members_to_df(group_name):
    wikidata_id = get_wikidata_id(group_name)
    members = get_members_from_wikidata(wikidata_id)
    return members






#### Webscrape function ####

def webscrape_members(band_title):

    url = f"https://da.wikipedia.org/wiki/{band_title.replace(' ', '_')}"

    # Fetch page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find infobox
    infobox = soup.find("table", class_="infobox")

    # Prepare dict for members
    members_data = ["Medlemmer", "Tidligere medlemmer"]
    members = []

    # Look through all rows in the infobox
    try:
        for row in infobox.find_all("tr"):
            header = row.find("th")
            if header:
                label = header.text.strip()
                if label in members_data:
                    data_cell = row.find("td")
                    if data_cell:
                        # Split lines or <br> tags into list items
                        items = [item.strip() for item in data_cell.stripped_strings]
                        members += items
    except:
        return []
    return members