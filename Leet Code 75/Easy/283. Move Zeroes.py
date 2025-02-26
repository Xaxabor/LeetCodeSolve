class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if nums[i]==0:
                break;
        for j in range(i+1,len(nums)):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i=i+1
