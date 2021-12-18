# create a tuple with supernatural characters - can't change

supernatural_characters = ("Bobby", "Castiel", "Crowley", "Dean", "Lilith", "Sam")

print(len(supernatural_characters))
print("Chuck" in supernatural_characters)
if "Lilith" in supernatural_characters:
    print(supernatural_characters.index("Lilith"))
else:
    print(-1)

if "Michael" in supernatural_characters:
    print(supernatural_characters.index("Michael"))
else:
    print(-1)

"""
Methods that don't work with tuples:
.append()
.clear()
.copy()
.clear()
.extend()
.insert()
.pop()
.remove()
.reverse()
.sort()
"""