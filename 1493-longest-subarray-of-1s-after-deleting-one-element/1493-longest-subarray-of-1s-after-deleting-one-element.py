class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1
        maxLen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen - 1