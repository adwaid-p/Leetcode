class Solution:
    def reverseWords(self, s: str) -> str:
        newString = ''
        listOfWords = s.split(' ')
        listOfWords = listOfWords[::-1]

        for word in listOfWords:
            if word != "":
                newString += word + " "
        return newString.strip()