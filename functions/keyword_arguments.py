# shorthand is kwargs (keyword arguments)

def about_character(character_name, character_type, character_age):
    return character_name + " is a " + character_type + " who is " + str(character_age) + \
           " years old."

print(about_character("Castiel", "angel", 400000000))

# you can pass in keyword arguments not in the exact order and it will still work.
print(about_character(character_age=50000000, character_name="Michael", 
      character_type="archangel"))

# you can also do this with variables
char_name = "Gabriel"
char_type = "archangel"
char_age = 450000000

print(about_character(character_type=char_type, character_age=char_age, character_name=char_name))

# Functions with lists

character_list = ["Castiel", "Crowley", "Sam", "Dean", "Michael", "Raphael", "Gabriel", "Chuck"]

def put_in_alp_order(char_list=[]):
    """ this function returns the list in alphabetical order """
    char_list.sort()
    return char_list

copy_char_list = character_list.copy()

print(put_in_alp_order(copy_char_list))

archangel_list = ["Raphael", "Michael", "Lucifer", "Gabriel"]

copy_arch_list = archangel_list.copy()

print(put_in_alp_order(copy_arch_list))

print(put_in_alp_order())  # this will print an empty list

def sort_in_alp_order(char_list=[]):
    """ this function returns the list in alp order, formatted better """
    char_list.sort()
    sorted_list = ''
    for name in char_list:
        sorted_list += name + ", "
    sorted_list = sorted_list[:-2]
    return sorted_list

print(sort_in_alp_order(copy_arch_list))
