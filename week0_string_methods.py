SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob squarepants",
    "Samurai X",
    "Naruto",
    "Jimmy neutron",
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    print(cleaned_shows)

main()