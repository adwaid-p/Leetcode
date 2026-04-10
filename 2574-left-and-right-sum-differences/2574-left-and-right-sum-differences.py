class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        answer = []
        total = sum(nums)
        left = 0
        
        for num in nums:
            right = total - left - num
            answer.append(abs(left - right))
            
            left += num
        
        return answer