# Remove Duplicates From an Unsorted Array

# Problem Statement: Given an unsorted array, remove duplicates from the array.

arr = [0,0,1,1,1,2,2,3,3,4,4,5]

result = []

for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
print(result)