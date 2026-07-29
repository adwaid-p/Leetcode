class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        candidates.sort()
        
        def backtrack(idx, rem_sum):
            if rem_sum == 0:
                res.append(curr.copy())
                return
            
            if rem_sum < candidates[idx]:
                return

            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, rem_sum - candidates[i])
                curr.pop()
        
        backtrack(0, target)
        return res