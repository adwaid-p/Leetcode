class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for l in range(min(len1, len2), 0, -1):
            if len1 % l == 0 and len2 % l == 0:
                factor1, factor2 = len1 // l, len2 // l
                if str1[:l] * factor1 == str1 and str1[:l] * factor2 == str2:
                    return str1[:l]
        return ""