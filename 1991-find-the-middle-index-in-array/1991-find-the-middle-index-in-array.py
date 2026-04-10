class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        arraySum = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = arraySum - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1