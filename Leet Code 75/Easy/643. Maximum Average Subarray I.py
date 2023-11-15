class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]

        maxS = sum
        l = 0
        r = k
        while(r<len(nums)):
            sum -=nums[l]
            sum +=nums[r]
            if maxS < sum:
                maxS = sum
            l, r = l+1, r+1
        
        return maxS/k
