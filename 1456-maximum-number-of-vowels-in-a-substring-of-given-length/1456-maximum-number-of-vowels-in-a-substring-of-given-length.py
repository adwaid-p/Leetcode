class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        maxVowels = 0
        crntVowels = 0
        for i in range(k):
            if s[i] in vowels:
                crntVowels += 1
        maxVowels = crntVowels

        for i in range(1,len(s) - k + 1):
            if s[i - 1] in vowels:
                crntVowels -= 1
            if s[i + k - 1] in vowels:
                crntVowels += 1
            maxVowels = max(crntVowels, maxVowels)
        return maxVowels