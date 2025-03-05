class Solution:
    def coloredCells(self, n: int) -> int:
        
        # def recurr(x):
        #     if x == 1:
        #         return 1
        #     return (4 * (x-1))+ recurr(x-1)
        
        # return recurr(n)

        return 1 if n==1 else 2 * (n-1)* n +1
