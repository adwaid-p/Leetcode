# Find Median of the given Array
# Problem Statement: Given an unsorted array, find the median of the given array.

arr = [4, 7, 1, 2, 5, 6, 8]
arr.sort()
print(arr)
n = len(arr)

if len(arr)%2 == 0:
    print((arr[n//2 - 1] + arr[n//2])/2)
else:
    print(arr[n//2])