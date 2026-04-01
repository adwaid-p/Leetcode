class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if stack and ch == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0