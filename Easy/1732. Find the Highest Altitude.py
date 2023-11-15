class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        max = 0
        sum = 0

        for i in gain:
            sum += i
            if max<sum:
                max = sum
        
        return max
        