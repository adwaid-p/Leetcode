class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        return len(freq) == len(set(freq.values()))