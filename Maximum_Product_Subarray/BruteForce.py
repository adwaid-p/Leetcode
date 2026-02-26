# Maximum Product Subarray in an Array

# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Nums = [1,2,-3,0,-4,-5]

max_prod = Nums[0]

for i in range(len(Nums)):
    cur_prod = 1
    for j in range(i, len(Nums)):
        cur_prod *= Nums[j]
        max_prod = max(cur_prod, max_prod)
print(max_prod)