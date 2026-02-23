# Find all repeating elements in an array

# Problem Statement: Find all the repeating elements present in an array.

arr = [1,1,2,3,4,4,5,2,5]
seen = {}
resulte = []

for i in range(len(arr)):
    if arr[i] in seen:
        seen[arr[i]] += 1
    else:
        seen[arr[i]] = 1

for key in seen:
    if seen[key] > 1:
        resulte.append(key)

print(resulte)