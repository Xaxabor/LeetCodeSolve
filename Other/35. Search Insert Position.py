class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        if target > nums[high]:
            return high+1

        if target == nums[high]:
            return high
        
        if target <= nums[low]:
            return low

        goRight = False

        while(high>=low):
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid -1
                goRight = False
            elif nums[mid] < target:
                low = mid+1
                goRight = True
            else:
                return mid
        if goRight:
            return mid + 1
        else:
            return mid