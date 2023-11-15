class Solution:

    def reverse(self, s: str) -> str:
        if s == " ":
            return ""
        return s[::-1]

    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        out = ""
        cur = ""

        for i in s:
            if i != " ":
                cur += i
            else:
                out = out + self.reverse(" "+cur)
                cur = ""

        # REMOVING FORWARD SPACE
        out= out + self.reverse(cur)
        newout =""
        ch = False 
        for i in out:
            if i is not " ":
                ch = True
            if ch is True:
                newout += i

        # REMOVING  SPACE
        newout = self.reverse(newout)
        out = ""
        ch = False 
        for i in newout:
            if i is not " ":
                ch = True
            if ch is True:
                out += i

        return self.reverse(out)
