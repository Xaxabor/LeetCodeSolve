class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        s = 0
        ans = ""
        d = len(a) - len(b)
        if d>0:
            b = (d * "0")+b
        else:
            a = ((-1)*d)*"0"+a
        
        for i in range(len(a)-1, -1, -1):
            sum = int(a[i])+int(b[i])+c
            if sum==1:
                s = 1
                c = 0
            elif(sum==2):
                s = 0
                c = 1
            elif(sum==3):
                s = 1
                c = 1
            else:
                s = 0
                c = 0
            ans = str(s) + ans
        if c == 1:
            ans = "1" + ans
        return ans
