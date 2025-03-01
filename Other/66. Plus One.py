class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[len(digits)-1] == 9 :
            sum = 0
            for i in range(0, len(digits)):
                sum = 10 * sum + digits[i]
            sum = sum + 1
            j = len(str(sum))-1
            if j==len(digits):
                digits.append(0)
            while(j>=0):
                digits[j] = sum%10
                sum = sum//10
                j = j-1

        else:
            digits[len(digits)-1] = digits[len(digits)-1] +1
        
        return digits
