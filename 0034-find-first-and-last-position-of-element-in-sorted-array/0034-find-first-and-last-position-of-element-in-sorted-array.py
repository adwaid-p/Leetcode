from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            i = nums.index(target)  # Find the index of the first occurrence
            s = i
            l = s
            out = [-1, -1]

            while i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    l += 1
                else:
                    break
                i += 1

            out[0] = s
            out[1] = l
            return out
        except ValueError:
            # Target not found in the list
            return [-1, -1]
