class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = {}
        result = []

        for num in arr1:
            count_map[num] = count_map.get(num,0) + 1
        for num in arr2:
            result.extend([num]*count_map[num])
        arr1.sort()
        for num in arr1:
            if num not in arr2:
                result.append(num)
        # notpresent.sort()
        # result.extend(notpresent)
        return result