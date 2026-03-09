import requests

def main():
    artwork = input("Artwork: ")
    artwork = get_artworks(query=artwork, limit=3)
    for artwork in artwork:
        print(f"* {artwork}")

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": query, "limit": limit})
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request: ")
        return []

    content = response.json()
    return [artwork["title"] for artwork in content["data"]]

main()