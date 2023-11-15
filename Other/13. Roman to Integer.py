class Solution:
    def romanToInt(self, s: str) -> int:

        # 1, 2, 3, 5, 7

        # O(n) comlexiety and O(7) memory to maitain the Hashmap

        map = { "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000 
               }             

        if len(s) == 1:
            return map[s]

        i = 0
        sum = 0
        while(len(s)-1>i):
            if(map[s[i]]>= map[s[i+1]]):
                sum += map[s[i]]
            else:
                sum -= map[s[i]]
            i += 1

        sum += map[s[i]]
        
        return sum


        