# Remove Duplicates in-place from Sorted Array

# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
nums = [0,0,1,1,1,2,2,3,3,4,4,5]

seen = set()

index = 0
for num in nums:
    if num not in seen:
        seen.add(num)
        nums[index] = num
        index += 1
print(nums[:len(seen)])