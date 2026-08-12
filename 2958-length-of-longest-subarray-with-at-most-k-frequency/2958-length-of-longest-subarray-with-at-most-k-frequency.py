from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frq = defaultdict(int)
        left = 0
        maxLen = 0

        for right, num in enumerate(nums):
            frq[num] += 1
            
            while frq[num] > k:
                frq[nums[left]] -= 1
                left += 1
                
            maxLen = max(maxLen, right - left + 1)

        return maxLen