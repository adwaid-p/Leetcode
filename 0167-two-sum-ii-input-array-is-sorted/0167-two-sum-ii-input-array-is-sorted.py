class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            number = target - numbers[i]
            if number in hashMap:
                return [hashMap[number],i + 1]
            else:
                hashMap[numbers[i]] = i + 1
        return []