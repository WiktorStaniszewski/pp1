import json
movie = {
    "title":"Forrest Gump",
    "year": 1994,
    "actor":{"leading":"Tom Hanks","supporting":"Robin Wright"},
    "oscar":True,
}

with open("favourite.json", 'w') as kfc:
    json.dump(movie,kfc)