class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        oddEven = 0
        # i, j = 0, 0
        out = ""

        while((oddEven//2) <len(word1) and (oddEven//2) <len(word2)):

            if oddEven % 2 == 0 :
                out += word1[oddEven//2]
                #i +=1
            else:
                out += word2[oddEven//2]
                #j +=1

            oddEven +=1

        out += word1[oddEven//2:]
        out += word2[oddEven//2:]

        return out