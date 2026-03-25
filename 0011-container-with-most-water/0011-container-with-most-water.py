class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            currWater = (right - left) * min(height[left], height[right])
            maxWater = max(currWater, maxWater)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater