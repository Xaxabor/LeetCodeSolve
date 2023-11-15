class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i] != " ":
                count +=1
            else:
                if count > 0:
                    ans = count
                    count = 0
        if count > 0:
            ans = count
                
        return ans