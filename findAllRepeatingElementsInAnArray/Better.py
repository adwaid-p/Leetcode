# Find all repeating elements in an array

# Problem Statement: Find all the repeating elements present in an array.

arr = [1,1,1,1,2,3,4,4,5,2,5,3,1]
result =[]
count = 0

arr.sort()
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]: 
        if count < 1:       #or check the last element of the result array and the arr[i] for avoiding duplicates in result
            result.append(arr[i])
            count += 1
    else:
        count = 0
print(result)