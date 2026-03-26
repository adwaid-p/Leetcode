class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        crntSum = maxSum

        for left in range(1,len(nums) - k + 1):
            right = left + k - 1
            crntSum = crntSum - nums[left - 1] + nums[right]
            maxSum = max(crntSum, maxSum)
        return maxSum / k