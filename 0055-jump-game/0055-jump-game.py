class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        i = len(nums) - 2
        while i >= 0:
            for j in range(1, nums[i] + 1):
                if i + j == end:
                    end = i
                    break
            i -= 1
        
        return end == 0