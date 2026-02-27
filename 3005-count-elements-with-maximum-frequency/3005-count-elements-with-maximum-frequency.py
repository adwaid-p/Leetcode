class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frq_map = {}
        maxfrq = 0
        total = 0
        for i in range(len(nums)):
            frq_map[nums[i]] = frq_map.get(nums[i], 0) + 1
            maxfrq = max(maxfrq, frq_map[nums[i]])
        for num in frq_map:
            if frq_map[num] == maxfrq:
                total += maxfrq
        return total