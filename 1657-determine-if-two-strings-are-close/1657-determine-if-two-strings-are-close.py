class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        frq1 = {}
        frq2 = {}

        for ch in word1:
            frq1[ch] = frq1.get(ch, 0) + 1
        for ch in word2:
            frq2[ch] = frq2.get(ch, 0) + 1
        # frq1 = dict(sorted(frq1.items()))
        # frq2 = dict(sorted(frq2.items()))
        if sorted(frq1.values()) == sorted(frq2.values()) and set(frq1.keys()) == set(frq2.keys()):
            return True
        else:
            return False