class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        if len(s) != len(t):
            return False
        for char in s:
            seen1[char] = seen1.get(char,0) + 1
        for char in t:
            if char in seen1:
                seen1[char] -= 1
            else:
                return False
            if seen1[char] < 0:
                return False
        return True