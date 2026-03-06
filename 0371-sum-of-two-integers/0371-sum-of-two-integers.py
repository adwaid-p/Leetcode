class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            sumWithoutCarry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a = sumWithoutCarry
            b = carry
        if a > MAX_INT:
            return ~(a ^ MASK)
        return a