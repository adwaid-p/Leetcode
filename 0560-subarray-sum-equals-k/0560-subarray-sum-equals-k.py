class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        ps = [0]*len(nums)
        frq_map = {}
        ps[0] = nums[0]
        for i in range(1,len(nums)):
            ps[i] = ps[i - 1] + nums[i]
        
        for j in range(len(nums)):
            if ps[j] == k:
                count += 1
            
            val = ps[j] - k
            if val in frq_map:
                count += frq_map[val]
            frq_map[ps[j]] = frq_map.get(ps[j],0) + 1
        return count
