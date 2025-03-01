class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j = -1
        for i in range (0, len(nums)-1):
            if nums[i]== nums[i+1]:
                nums[i], nums[i+1] = 2 * nums[i], 0

        # solution 1 : if item is not zero then keep adding it from first index and then make remaining index zero
        # for i in range (0, len(nums)):
        #     if nums[i]!=0:
        #         nums[j] = nums[i]
        #         j = j+1
        
        # while(len(nums)>j):
        #     nums[j] = 0
        #     j = j+1

        # solution 2 : find out first zero and then keep checking if current item is non zero and swap with the zero items
        for i in range (0, len(nums)):
            if nums[i] == 0:
                j = i
                break;    
        if j==-1:
            return nums
        for i in range(j+1, len(nums)):
            if nums[i] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                j = j + 1

        return nums
        
