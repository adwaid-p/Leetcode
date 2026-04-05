from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(n + r)
            else:
                dire.append(n + d)
        return "Radiant" if radiant else "Dire"