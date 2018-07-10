def uni_char(str):
    count_map = dict.fromkeys(set(str), 0)
    for letter in str:
        count_map[letter] += 1

    for key, value in count_map.items():
       if value > 1:
           return False
       else:
           return True
 
 
print(uni_char("AAABCCDDDDD"))
