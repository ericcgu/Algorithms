#Code Challenge:
#  Implement a function to find the most frequent character or letter in a string.
#  Only consider characters, not spaces or punctuation. Consider capital letters to be the same as lower case.
#Example:
#  max_char('Hello !') === 'l'

def max_char(string):
    max_char = ''
    max_count = 0

    character_map = dict.fromkeys(clean_string(string),0)
    for character in clean_string(string):
        character_map[character] += 1

    for key, value in character_map.items():
        if value > max_count:
            max_char = key
            max_count = value
    return max_char



def clean_string(string):
    import string as stringlib
    for char in stringlib.punctuation:
        string = string.replace(char,'')
    return string.lower()






print(max_char('Hello !'))

















print('Passed Test 1' if max_char('Hello !') == 'l' else 'Test 1 Incomplete')



