supernatural_characters = {"Bobby", "Sam", "Dean", "Crowley", "Castiel"}

print(len(supernatural_characters))

"""
can't get index of a set
can't use sort or reverse
can add if item not in set
"""

supernatural_characters.add("Meg")

print(supernatural_characters)

supernatural_characters.add("Meg")

second_sup_char_list = supernatural_characters.copy()

print(second_sup_char_list)