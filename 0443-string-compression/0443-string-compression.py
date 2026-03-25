class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        idx = 0
        while i < n:
            char = chars[i]
            count = 0
            while i < n and chars[i] == char:
                i += 1
                count += 1
            
            chars[idx] = char
            idx += 1
            
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        return idx