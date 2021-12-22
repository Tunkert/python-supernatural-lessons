# Create a variable for a new name that you want to append
new_character_name = 'Chuck\n'  # add the slash n to create a line break
# open names.txt in append mode with utf-8 encoding
with open('supernatural_names.txt', 'a', encoding='utf-8') as f:
    f.write(new_character_name)
