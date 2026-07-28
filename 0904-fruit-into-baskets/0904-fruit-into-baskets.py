class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = end = 0
        bucket = {}
        maxL = 0
        
        while end < len(fruits):
            
            bucket[fruits[end]] = bucket.get(fruits[end], 0) + 1
            
            while len(bucket) > 2:
                bucket[fruits[start]] -= 1
                if bucket[fruits[start]] ==0:
                    del bucket[fruits[start]]
                start += 1
                
            maxL = max(maxL, end-start+1)
            end += 1

        return maxL