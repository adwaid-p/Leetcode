# Maximum Subarray Sum Problem

# Problem Statement:
# Given an array of integers (which may include both positive and negative numbers),
# find the contiguous subarray that has the largest possible sum and return that sum.

arr = [3,-4,5,4,-1,7,-8]

count = 0
max_sum = float('-inf')

for start in range(len(arr)):
    curr_sum = 0
    for end in range(start,len(arr)):
        curr_sum += arr[end]
        max_sum = max(max_sum, curr_sum) 
print(max_sum)
