# Maximum Product Subarray in an Array

# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

Nums = [3, -1, 4]

pre, suff = 1, 1
max_prod = float('-inf')
ans = 0

for i in range(len(Nums)):
    
    pre *= Nums[i]
    suff *= Nums[len(Nums) - 1 - i]

    ans = max(ans, pre, suff)

    if pre == 0:
        pre = 1
    if suff == 0:
        suff = 1
print(ans)