#Code Challenge:
#Implement a function to find the longest common prefix in an array of strings.

#Examples:
#longest_common_prefix(["patty","patricia","patrick"]) === 'pat'
#longest_common_prefix(["j","joeblack","joebrown"]) === 'j'
#longest_common_prefix(["dog","racecar","car"]) === ''
#*assume no inputs have capitals or spaces

def longest_common_prefix(strings):
    lcp = min(strings, key=len)
    while len(lcp) > 0:
        number_of_string_matches = 0

        for string in strings:
            if string[:len(lcp)] == lcp:
                number_of_string_matches += 1

        if number_of_string_matches == len(strings):
            return lcp

        lcp = lcp[:len(lcp)-1]
    return ''











print('Passed Test 1' if longest_common_prefix(["patty","patricia","patrick"]) == 'pat' else 'Test 1 Incomplete')
print('Passed Test 2' if longest_common_prefix(["j","joeblack","joebrown"]) == 'j' else 'Test 2 Incomplete')
print('Passed Test 3' if longest_common_prefix(["dog","racecar","car"]) == '' else 'Test 3 Incomplete')