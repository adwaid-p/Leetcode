class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        prev = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            prev = max(count, prev)
        return prev 
        