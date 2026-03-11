class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                result.append(i)
        return result