class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frq = {}
        maxLen = 0
        left = 0

        for right in range(len(nums)):
            frq[nums[right]] = frq.get(nums[right],0) + 1
            
            while frq[nums[right]] > k:
                frq[nums[left]] -= 1
                left += 1
                
            maxLen = max(maxLen, right - left + 1)

        return maxLen