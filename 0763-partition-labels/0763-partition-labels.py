class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        size = end = 0
        res = []

        for i, c in enumerate(s):
            index[c] = i
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, index[c])

            if i == end:
                res.append(size)
                size = 0
        return res