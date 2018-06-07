""" Code Challenge:
Implement a function that determines if the integer parameter is a palindrome.
Coud you solve it without converting the integer to a string?

Examples:
palindrome(121) === True
palindrome(50) === False
palindrome(-121) === False
"""

def palindrome(integer):
    if ( integer < 0):
        return False
    container = []
    n = integer
    while n > 0:
        container.append(n % 10)
        n =  n // 10
    return container == container[::-1]

print(palindrome(121))
print(palindrome(121))