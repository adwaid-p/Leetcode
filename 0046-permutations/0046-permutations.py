class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def permutation():
            if len(current) == len(nums):
                result.append(current[:])
                return
            for num in nums:
                if num in current:
                    continue
                current.append(num)
                permutation()
                current.pop()
        permutation()
        return result