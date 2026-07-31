class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        i = len(nums) - 2
        while i >= 0:
            if nums[i] + i >= end:
                end = i
            i -= 1
        
        return end == 0