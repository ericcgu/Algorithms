def finder(arr1, arr2):
    for a, b in zip(sorted(arr1), sorted(arr2)):
        if a != b:
            return a

print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))