class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        mulwithout0 = 1
        count = 0
        for i in nums:
            mul *=i
            if i == 0:
                count +=1
            else:
                mulwithout0 *= i
        
        if count > 1 :
            a = len(nums)
            nums = ()
            nums = [0]*a
            return nums
        else:
            for i in range(len(nums)):
                if nums[i] !=0:
                    nums[i] = mul//nums[i]
                else:
                    nums[i]= mulwithout0
            return nums