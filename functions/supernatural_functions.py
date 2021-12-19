def hello_chuck():  # simple function, passing in no arguments
    return "Hello Chuck"

def hello_character(character_name): #simple function, passing in one argument
    return "Hello " + character_name

def unsink_titanic(number_of_souls_owned):
    """ This function shows how many souls Castiel has after Balthazar unsinks the titanic """
    souls_gained = 50000  # local to function
    number_of_souls_owned += souls_gained
    return number_of_souls_owned

say_hello_to_god = hello_chuck()

print(say_hello_to_god)
number_of_souls_owned = 0

say_hello = hello_character("Castiel")
print(say_hello)

castiel_s6_souls = unsink_titanic(number_of_souls_owned)
print(castiel_s6_souls)
castiel_s6_souls = unsink_titanic(100000)  # will output 150000

print(castiel_s6_souls)
# print(souls_gained)  # this will throw an error

def unsink_boat(souls_orig, souls_add):
    total_souls = souls_orig + souls_add
    return total_souls

castiels_new_soul_count = unsink_boat(50000, 20000)
print(castiels_new_soul_count)

print("Castiel now has " + str(castiels_new_soul_count) + " souls.")

print(f"Castiel now has {unsink_boat(30000, 200000)} souls.")

