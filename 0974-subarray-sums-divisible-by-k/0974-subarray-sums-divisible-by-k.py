class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefixSum = [0] * len(nums)
        frq_map = {}

        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        for j in range(len(nums)):
            
            if (prefixSum[j] % k + k) % k == 0:
                count += 1
            
            val = (prefixSum[j] % k + k) % k
            if val in frq_map:
                count += frq_map[val]
            
            frq_map[val] = frq_map.get(val, 0) + 1

        return count