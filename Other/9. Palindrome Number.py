class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            sum = 0
            n = x
            while(n>0):
                sum = 10*sum + n%10
                n = n//10
            print(sum)
            if x==sum:
                return True
            else:
                return False


