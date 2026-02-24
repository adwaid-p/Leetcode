# Find all Symmetric Pairs in the array of pairs

# Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.

arr = [(1,2),(2,1),(3,4),(4,5),(5,4)]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]:
            print(arr[i], end=" ")