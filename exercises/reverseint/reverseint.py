import numpy
def reverseInt(n):
    x = list(str(abs(n)))
    x.reverse()
    return int(''.join(x)) * numpy.sign(n)

print(reverseInt(-16))
print(reverseInt(15))
print(reverseInt(500))