""" Code Challenge:
Implement a function that reverses the order of the digit values.

reverseInt(456) === 654
reverseInt(700) === 7
reverseInt(-123) === -321
reverseInt(-90) === -9  
"""

def reverse_int(integer):
    sign = [1, -1][integer < 0]
    return int(str(abs(integer))[::-1]) * sign

print(reverse_int(456))
print(reverse_int(700))
print(reverse_int(-123))




































print('Passed Test 1' if reverse_int(456) == 654 else 'Test 1 Incomplete')
print('Passed Test 2' if reverse_int(700) == 7 else 'Test 2 Incomplete')
print('Passed Test 3' if reverse_int(-123) == -321 else 'Test 3 Incomplete')
print('Passed Test 4' if reverse_int(-900) == -9 else 'Test 4 Incomplete')
