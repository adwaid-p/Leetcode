class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = totalCost = 0

        for g in gas:
            totalGas += g
        
        for c in cost:
            totalCost += c
        
        if totalGas < totalCost:
            return -1
        
        start = currGas = 0
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                start = i + 1
                currGas = 0
        
        return start