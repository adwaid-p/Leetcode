# Rearrange array in increasing-decreasing order
# Problem Statement: Rearrange a given array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order

arr = [1,2,3,4,5,6,7,8]
arr.sort()

i = len(arr)//2
j = 0

while i < 3*len(arr)//4:
    arr[i], arr[len(arr)-1-j] = arr[len(arr)-1-j], arr[i]
    i += 1
    j += 1
print(arr)