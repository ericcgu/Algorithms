def chunk(array, n):
    return list(array[i:i+n] for i in range(0, len(array), n))  
    
print(chunk([1, 2, 3, 4, 5], 2))