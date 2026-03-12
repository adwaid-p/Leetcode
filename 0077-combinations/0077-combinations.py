class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []
        def findCombination(start):
            if len(current) == k:
                result.append(current.copy())
                return
            for i in range(start, n + 1):
                current.append(i)
                findCombination(i + 1)
                current.pop()
        findCombination(1)
        return result