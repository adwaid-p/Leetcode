# Maximum Subarray Sum Problem

# Problem Statement:
# Given an array of integers (which may include both positive and negative numbers),
# find the contiguous subarray that has the largest possible sum and return that sum.

#KADANE'S Algorithm

arr = [3,-4,5,4,-1,7,-8]

max_sum = float('-inf')
curr_sum = 0

for i in range(len(arr)):
    curr_sum += arr[i]
    max_sum = max(curr_sum, max_sum)
    if curr_sum < 0:
        curr_sum = 0

print(max_sum)