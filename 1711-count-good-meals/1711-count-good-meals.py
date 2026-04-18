class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7
        pairs = 0
        freq = {}
        powers = []

        for i in range(22):
            powers.append(2**i)

        for num in deliciousness:
            for power in powers:
                complement = power - num
                if complement in freq:
                    pairs += freq[complement]
                    pairs %= MOD

            freq[num] = freq.get(num, 0) + 1
        
        return pairs