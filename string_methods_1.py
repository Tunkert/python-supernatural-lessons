print("This is a string.")  # prints out "This is a string."
print("Castiel is an angel on Supernatural.")  # another string printed

# Escape characters
print("Dean says, \"hi!\"")  # need to use escape characters to print quotes
# within quotes

# newlines
print("Sam is possessed by Lucifer on Supernatural.\nThat's bad!")
# will print "That's bad on next line"

# normal backslash
print("This is a normal \ backslash.")  # prints out normal backslash

# lower case
char_name = "Dean"

print(char_name.lower())  # will print out "dean"

# upper case
angel_name = "Zachariah"

print(angel_name.upper())  # will print out "ZACHARIAH"

# check if string is lower case

print(angel_name.upper().islower())  # will print out False

# check if string is lower case

print(angel_name.lower().islower())  # will print out True

# check if string is upper case

print(angel_name.upper().isupper())  # will print out True

# check if string is upper case

print(char_name.lower().isupper())  # will print out False

# print out length of string

print(len(char_name))  # will print out 4

# will have index from 0 to 3

# print out character in string at certain position

print(char_name[0])  # prints out first character in string, D

print(angel_name[-1])  # prints out last character in string, h

print(char_name[-2])  # prints out 2nd character from end, a

# Other Methods #

demon_name = "crowley"

print(demon_name.capitalize())  # prints Crowley

sup_string = "Dean is Pretty COOL."

print(sup_string.casefold())  # prints "dean is pretty cool"

print(char_name.center(30, "-"))  # centers string in "-" character,
# total: 30 char

odd_string = "dean is dean and that is pretty dean."

print(odd_string.count("dean"))  # prints out 3

print(odd_string.encode(encoding="utf-16", errors="ignore"))  # prints utf-16
# encoding

print(odd_string.endswith("!"))  # will return False

print(odd_string.endswith("."))  # will return True
