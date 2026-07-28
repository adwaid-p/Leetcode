class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = end = 0
        maxL = 0

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                maxL = max(maxL, end - start + 1)
                end += 1
            else:
                seen.remove(s[start])
                start += 1

        return maxL
