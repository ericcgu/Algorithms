#Code Challenge:
#  Implement a function that groups anagrams together, given an array of strings. 

#Examples:
#  group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) --> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
#  or formatted version:        [
#                                   ["ate","eat","tea"],
#                                   ["nat","tan"],
#                                   ["bat"]
#                               ]
def group_anagrams(strings):
    group_map = {}
    for string in strings:
        key = ''.join(sorted(string))
        if key not in group_map:
            group_map[key] = [string] #if key is not in dictionary, initialize the first key value pair
        else:
            group_map[key] += [string] #if key does exist, add the raw string to existing array in dict value
    return list(group_map.values())
    

    



print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))











print('Passed Test 1' if group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] else 'Test 1 Incomplete')
