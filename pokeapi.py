import urllib.request
import json
import time

types = []
dic = {}


def getJson(url):
    request = urllib.request.Request(url)
    # must add this or the request will fail
    request.add_header('User-Agent', "cheese")
    data = urllib.request.urlopen(request).read()
    api = json.loads(data)
    return api


def addTypes(type):
    if type not in types:
        types.append(type)


def addToDic(type, pokemon):
    ls = []
    if(type in dic):
        ls = dic[type]
    ls.append(pokemon)
    dic.update({type: ls})


def listPokemons():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=151'
    api = getJson(url)
    for val in api["results"]:
        getPokemon(val["url"])


def getPokemon(url):
    print(url)
    api = getJson(url)
    name = api["name"]
    id = api["id"]

    for val in api["types"]:
        type = val["type"]["name"]
        addTypes(type)
        addToDic(type, {"id": id, "name": name})


listPokemons()
print(types)
print(dic)
