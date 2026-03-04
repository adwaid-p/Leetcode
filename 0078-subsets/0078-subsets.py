class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        ans = []
        def addSubset(nums, ans, i):
            if i == len(nums):
                result.append(ans.copy())
                return

            ans.append(nums[i])
            addSubset(nums, ans, i + 1)

            ans.pop()
            addSubset(nums, ans, i + 1)
        addSubset(nums,ans,0)
        return result