import string

x = 'hello'.lower()
chars = dict.fromkeys(string.ascii_lowercase, 0)
for s in x:
    chars[s]+= 1

chars = {x:y for x,y in chars.items() if y!=0}
maxValKey = max(chars, key=chars.get)
print(str(maxValKey))