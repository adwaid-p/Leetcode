# Find all Symmetric Pairs in the array of pairs

# Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.

arr = [(1,2),(2,1),(3,4),(4,5),(5,4)]

map = {}

for i in range(len(arr)):
    first, second = arr[i]
    if second in map and map[second] == first:
        print(f"({first}, {second})", end=" ")
    else:
        map[first] = second