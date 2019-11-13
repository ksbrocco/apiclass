import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():

    gotresp = requests.get(AOIF_BOOKS)

    got_dj = gotresp.json()

    for singlebook in got_dj:
        print(singlebook["name"] + ",", "pages -", singlebook["numberOfPages"])

if __name__ == "__main__":
    main()
