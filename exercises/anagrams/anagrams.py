#Code Challenge:
#  Implement a function to check to see if two strings are anagrams of each other.
#  One string is an anagram of another if it uses the same characters in the same quantity. 
#  Only consider characters, not spaces or punctuation. Consider capital letters to be the same as lower case.

#Examples:
#  are_anagrams('Public relations', 'Crap built on lies.') --> True
#  are_anagrams('Career politicians', 'No special criteria.') --> True
#  are_anagrams('Sangram', 'Kakade') --> False

def are_anagrams(string1, string2):
    return character_map(string1) == character_map(string2)

def character_map(string):
    character_map = dict.fromkeys(clean_string(string),0)
    for character in clean_string(string):
        character_map[character]+= 1
    return character_map
    
def clean_string(string):
    import string as stringlib
    for char in stringlib.punctuation:
        string = string.replace(char,'').replace(' ', '')
    return string














print('Passed Test 1' if are_anagrams('Public relations', 'Crap built on lies.') == True else 'Test 1 Incomplete')
print('Passed Test 2' if are_anagrams('Career politicians', 'No special criteria.') == True else 'Test 2 Incomplete')
print('Passed Test 3' if are_anagrams('Sangram', 'Kakade')  == False else 'Test 3 Incomplete')
