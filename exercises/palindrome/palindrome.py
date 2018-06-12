""" Code Challenge:
Implement a function that determines if the integer parameter is a palindrome.
Coud you solve it without converting the integer to a string?

Examples:
palindrome(121) === True
palindrome(50) === False
palindrome(-121) === False
"""

def palindrome(integer):
    if integer < 0:
        return False
    result = []
    i = integer
    while i > 0:
        result.append(i % 10)
        i = i // 10
    return result == result[::-1]

print(palindrome(121))
print(palindrome(50))
print(palindrome(-121))






















print('Passed Test 1' if palindrome(121) == True else 'Test 1 Incomplete')
print('Passed Test 1' if palindrome(99) == True else 'Test 1 Incomplete')
print('Passed Test 2' if palindrome(10) == False else 'Test 2 Incomplete')
print('Passed Test 3' if palindrome(-123) == False else 'Test 3 Incomplete')

