class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        ans = []
        nums.sort()
        def addSubset(nums,ans,i):
            if i == len(nums):
                result.append(ans.copy())
                return
            
            ans.append(nums[i])
            addSubset(nums,ans,i + 1)

            ans.pop()

            idx = i + 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1
            
            addSubset(nums, ans, idx)
            
        addSubset(nums, ans, 0)
        return result