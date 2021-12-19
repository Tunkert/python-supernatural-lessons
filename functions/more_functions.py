def alphabeticize_characters(*args):
    char_list = list(args)
    char_list.sort()
    char_output = ''
    for character in char_list:
        char_output += character + ", "
    char_output = char_output[:-2]
    return char_output

print(alphabeticize_characters("Castiel", "Amadeus", "Lilith", "Gabriel", "Michael", "Dean", "Sam", "Chuck"))

print(alphabeticize_characters("John Mclane", "Hans Gruber", "Argyle", "Holly", "Karl"))

