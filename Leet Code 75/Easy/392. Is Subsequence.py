class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0
        if s == t: 
            return True
        if s is None or t is None:
            return False
        
        while(si<len(s) and ti<len(t)):
            if s[si] == t[ti]:
                si, ti= si+1, ti+1
            else:
                ti += 1
        
        if si == len(s):
            return True
        else:
            return False
        