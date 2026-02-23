# Find all repeating elements in an array

# Problem Statement: Find all the repeating elements present in an array.

arr = [5, 2, 5, 2, 5]
dup = []

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            dup.append(arr[j])

dup.sort()

for i in range(len(dup)):
    if i == 0 or dup[i] != dup[i - 1]:
        print(dup[i], end=' ')