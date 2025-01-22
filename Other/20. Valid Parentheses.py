class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")" : "(",
            "}" : "{",
            "]" : "[" 
        }
        temp = []

        for i in range(0, len(s)):
            if(s[i]=='(' or s[i]== "{" or s[i]== "["):
                temp.append(s[i])
            elif s[i] in map:
                if len(temp) > 0:
                    tempLast = temp[len(temp)-1]
                    if (tempLast == map[s[i]]):
                        temp.pop()
                    else:
                        return False
                else:
                    return False
        if len(temp) == 0:
            return True
        else:
            return False
