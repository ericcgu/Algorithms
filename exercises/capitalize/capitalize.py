import datetime

def pair_sum(arr, value):
    seen = set()
    output = set()
    for item in arr:
        target = value - item
        if target not in seen:
            seen.add(item)
        else:
            output.add( (min(item,target), max(item,target)))
    return output

print(pair_sum([1,3,2,2], 4))
