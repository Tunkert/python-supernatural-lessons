import json

with open('breweries-lite.json', 'r', encoding='utf-8', newline='') as brew_file:
    brews = json.load(brew_file)

colorado_brews = open("colorado_brews.txt", "a", encoding="utf-8")
for brew in brews:
    if brew['state'] == "Colorado":
        colorado_brews.write(brew['name'] + ", " + brew['city'])
        colorado_brews.write("\n")

colorado_brews.close()
