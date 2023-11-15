class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("-123")
        j=0
        c = 1
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                c +=1
            else:
                chars[j]= chars[i]
                j = j+1
                if c>1 and c<10:
                    chars[j]= str(c)
                    j = j+1
                elif c >= 10 :
                    for k in str(c):
                        chars[j]= str(k)
                        j = j+1
                c = 1

        return len(chars[:j])