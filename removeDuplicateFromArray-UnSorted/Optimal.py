# Remove Duplicates From an Unsorted Array

# Problem Statement: Given an unsorted array, remove duplicates from the array.

arr = [0,0,1,1,1,2,2,3,3,4,4,5,6]

seen = {}
result = []

for num in arr:
    if num not in seen:
        seen[num] = True
        result.append(num)
print(result)