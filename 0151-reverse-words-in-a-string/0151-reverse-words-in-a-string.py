class Solution:
    def reverseWords(self, s: str) -> str:
        newString = ''
        string = []
        s = list(s)
        for i in range(len(s)):
            if s[i] != ' ':
                newString += s[i]
            else:
                if newString:
                    string.append(newString)
                newString = ''
        if newString:
            string.append(newString)
        left = 0
        right = len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        return ' '.join(string)