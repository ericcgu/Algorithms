def largestsum(arr):
    largest_sum = None
    rolling_count = 0
    for num in arr:
        rolling_count += num
        if largest_sum == None or rolling_count > largest_sum:
            largest_sum = rolling_count
            rolling_count = 0
    return largest_sum

print(largestsum([1,2,-1,3,4,10,10,-10,-1]))

        