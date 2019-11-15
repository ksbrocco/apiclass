#!/usr/bin/python3

import requests

POKEURL = "http://pokeapi.co/api/v2/pokemon/?limit=964"

def getpokemon():

    resp = requests.get(POKEURL)
    resp = resp.json()
   
    pokedex = []
    for pokemon in resp.get("results"):
        pokedex.append(pokemon.get("name"))
    return pokedex

def main():

    pokedex = getpokemon()
    for pokemon in pokedex:
        print(pokemon)

if __name__ == "__main__":
    main()
