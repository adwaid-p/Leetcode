class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        for i in range(len(gain)):
            altitude.append(gain[i] + altitude[i])
        return max(altitude)