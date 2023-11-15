class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = {}
        if(k == 0):
            return False

        for i in range(len(nums)):
            if nums[i] in map:
                if (i - map[nums[i]]) <= k:
                    return True
            map[nums[i]] = i

        return False