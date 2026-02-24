# Find all the non-repeating elements in an array

# Problem Statement: Find all the non-repeating elements for a given array. Outputs can be in any order.

Nums = [1,2,-1,1,3,1]

count = {}

for num in Nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num in count:
    if count[num] == 1:
        print(num, end=',')