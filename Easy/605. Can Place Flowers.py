class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        if n == 0 :
            return True

        if len(flowerbed) == 1 and flowerbed[0]==0 and n==1:
            return True
        
        if len(flowerbed) == 1 and flowerbed[0]==1 and n>0:
            return False

        prev = 0
        for i in range(len(flowerbed)-1):   
            if flowerbed[i] == 0 and prev == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            prev = flowerbed[i]
            if n == 0:
                return True
        
        if (n==1) and flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            return True

        return False