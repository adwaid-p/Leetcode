# Remove Duplicates in-place from Sorted Array

# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

nums = [0,0,1,1,1,2,2,3,3,4,4,5]

l = 0

for i in range(1,len(nums)):
    if nums[i] != nums[l]:
        l += 1
        nums[l] = nums[i]
print(nums)