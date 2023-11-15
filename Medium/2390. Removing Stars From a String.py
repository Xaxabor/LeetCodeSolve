class Solution:
    def removeStars(self, s: str) -> str:
        out =""
        for i in s:
            if i == "*":
                out = out[:-1]
            else:
                out += i
        return out
