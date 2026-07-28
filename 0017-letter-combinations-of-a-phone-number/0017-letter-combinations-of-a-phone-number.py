class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = { 2 : "abc",3 : "def", 4 :"ghi", 5: "jkl", 6 : "mno",7 : "pqrs",8 : "tuv",9 : "wxyz" }
        
        n = len(digits)
        diary = []
        ans = []
        
        def combination(idx):
            if idx == n:
                ans.append("".join(diary))
                return
            
            letterComp = dic[int(digits[idx])]
            for i in range(len(letterComp)):
                diary.append(letterComp[i])
                combination(idx + 1)
                diary.pop()
        combination(0)
        return ans
                