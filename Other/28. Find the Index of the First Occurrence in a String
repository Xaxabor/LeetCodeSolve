class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        ni = 0
        index = -1
        while(i<len(haystack)):
            if haystack[i]==needle[ni]:
                ni=ni+1
                if len(needle) == ni:
                    index = i + 1 - ni
                    break
            else:
                i = i - ni
                ni = 0
            i= i+1
        return index
