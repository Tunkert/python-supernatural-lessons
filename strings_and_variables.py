# Supernatural lesson - strings with variables

# We'll discuss printing out strings, Concatenation, and f strings.

"""
potential character names:
angel - Uriel, Bartholemew, Zachariah, Metatron
human - sam, dean, bobby, jo, Mary
demon - Meg, Lilith, Crowley, Azazel, Alastair, Ramiel, Dagon, Asmodeus
archangel - Michael, Lucifer, Raphael, Gabriel
"""

print("Castiel is an angel on Supernatural.")
print("Dean is a human on Supernatural")
print("Crowley is a demon on Supernatural")
print("Gabriel is an archangel on Supernatural")

# Let's say we want to change the names.
# We can rewrite this with variables

# Variables
angel = "Castiel"
human = "Dean"
demon = "Crowley"
archangel = "Gabriel"


# Concatenation method - pre 3.6
print(angel + " is an angel on Supernatural.")
print(human + " is an human on Supernatural.")
print(demon + " is an demon on Supernatural.")
print(archangel + " is an archangel on Supernatural.")


# Alternative method
print(angel, " is an angel on Supernatural.")
print(human, " is a human on Supernatural.")
print(demon, " is a demon on Supernatural.")
print(archangel, " is an archangel on Supernatural.")


# 3.6 and higher
print(f"{angel} is an angel on Supernatural.")
print(f"{human} is a human on Supernatural.")
print(f"{demon} is a demon on Supernatural.")
print(f"{archangel} is an archangel on Supernatural.")


# Variables allow you to change character names.
angel = "Anna"
human = "Sam"
demon = "Lilith"
archangel = "Raphael"


# print with new names
print(f"{angel} is an angel on Supernatural.")
print(f"{human} is a human on Supernatural.")
print(f"{demon} is a demon on Supernatural.")
print(f"{archangel} is an archangel on Supernatural.")
