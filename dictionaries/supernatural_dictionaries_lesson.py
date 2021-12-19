"""
Hi, my name is Timothy Unkert and Welcome to my channel, in this
video we are going to cover Python dictionaries. The Python dictionaries
I'm going to cover will be based on characters from my favorite t.v. show,
Supernatural.
Dictionaries are another way to store value through key, value pairs,
they take the basic
structure of:
dictionary_name = {
    'key_name' = value,
    'key_name' = value,
    'key_name' = value,
    'key_name' = value
}
"""

castiel = {
    'type': "angel",
    'age': 400000000,
    'status': "alive"
}

dean = {
    'type': "human",
    'age': 41,
    'status': "dead"
}

crowley = {
    'type': "demon",
    'age': 356,
    'status': "dead"
}

print(crowley['age'])  # prints value for 'age' key in crowley dictionary
character_status = 'status'  # assigns variable to key 'status'
print(castiel['status'])  # prints the 'status' value of castiel dictionary
print(castiel[character_status])  # prints the same as line above
print(len(crowley))  # prints the length of the crowley dictionary
print('demeanor' in crowley)
print(dean.get('status'))  # won't crash if key is not there, see below
print(dean.get('demeanor'))  # prints None
print(dean.get('status', 'Sorry I can\'t find that.'))  # will print 'dead'
print(dean.get('demeanor', 'Sorry, I can\'t find that.'))  # will print Sorry \
#  ...

# changing the value of a key
dean['status'] = "in heaven"  # changes 'status' value to "in heaven"
print(dean.get('status'))  # prints "in heaven"

# adding or changing dictionary data
dean.update({'status': "alive"})  # changes 'status' value to alive

print(dean.get('status'))  # prints alive
dean.update({'demeanor': "cool"})  # adds key value pair

print(dean.get('demeanor', 'Sorry I can\'t find that.'))  # prints cool
print(dean)  # prints entire dictionary named dean

# loop through dictionary, printing keys
for item in dean:
    print(item)

# loop through dictionary, printing values method
for item in dean.values():
    print(item)

# loop through dictionary, printing keys and values with items method
for characteristic in dean.items():
    print(characteristic)

# loop through dictionary printing keys and values, better formatting
for key, value in dean.items():
    print(key, "=", value)

# copy a dictionary
alternate_world_michael = dean.copy()
print(alternate_world_michael)

# clear a dictionary
alternate_world_michael.clear()
print(alternate_world_michael)  # after Jack uses the power of his soul to
# destroy alternate world michael

# returns a copy with only specified keys
keys = {'status'}
values_list = "dead"
alternate_world_michael = dean.fromkeys(keys, values_list)
print(alternate_world_michael)
# more on this below - maybe don't hit this yet

# pop method
castiels_status = castiel.pop('status')
print(castiels_status)

# del method
del castiel["age"]  # gets rid of key "age" in castiel dictionary
print(castiel)

# be careful with del method - if you del dean, entire dean dictionary would be deleted.
# I can type this line then comment it out with gcc

# more on fromkeys
gabriel = dict.fromkeys(['type', 'status', 'age', 'demeanor'])
print(gabriel)

# can use a standard set of keys to create new dictionaries
character = {
        'type': 'human',
        'age': 30,
        'status': 'alive',
        'demeanor': 'whiny'
        }

michael = dict.fromkeys(character.keys())
print(michael)

# setdefault() method
raphael = dict.fromkeys(character.keys())
raphael.setdefault('type', "angel")
raphael.setdefault('age', 400000000)
raphael.setdefault('status', 'dead')
raphael.setdefault('title', 'ruler of heaven')  # this is the only item that will change
print(raphael)

# nesting dictionaries
supernatural_characters = {
        'dean': {
            'type': 'human',
            'age': 41,
            'status': 'in heaven',
            'demeanor': 'cool'
            },
        'sam': {
            'type': 'human',
            'age': 80,
            'status': 'in heaven',
            'demeanor': 'whiny'
            },
        'gabriel': {
            'type': 'archangel',
            'age': 400000000,
            'status': 'dead',
            'demeanor': 'funny'
            },
        'crowley': {
            'type': 'demon',
            'age': 356,
            'status': 'dead',
            'demeanor': 'evil'
            }
        }

for character in supernatural_characters.keys():
    print(character)

for key in supernatural_characters.keys():
    print(key + ":")
    print("    " + supernatural_characters[key]['type'])
    print("    " + str(supernatural_characters[key]['age']))
    print("    " + supernatural_characters[key]['status'])
    print("    " + supernatural_characters[key]['demeanor'])

