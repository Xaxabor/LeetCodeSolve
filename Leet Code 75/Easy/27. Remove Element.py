class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # looking for first val match
        count = 0
        valIndex = 0
        for i in range(len(nums)):
            if nums[i] == val:
                valIndex = i
                break;
            else:
                count = count + 1
        
        for j in range(valIndex+1, len(nums)):
            if nums[j]!=val:
                nums[valIndex], nums[j] = nums[j], nums[valIndex]
                valIndex=valIndex+1
                count = count + 1

        return count
