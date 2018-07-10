def largestsum(arr):
    max_sum = current_sum = arr[0]
    start = 0
    end = 0
    for i, num in enumerate(arr[1:]):
        current_sum = max(current_sum + num, num)

        max_sum = max(current_sum, max_sum)

        if current_sum > max_sum:
            

    return max_sum

print(largestsum([1,2,-1,3,4,10,10,-10,-1]))

        