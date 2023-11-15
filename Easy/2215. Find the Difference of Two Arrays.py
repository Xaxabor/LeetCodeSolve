class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        s1 , s2 = set(nums1), set(nums2)
        l1 = list() 
        out= list()

        for i in s1:
            if(i not in s2):
                l1.append(i)
        
        out.append(l1)

        l1 = list() 

        for i in s2:
            if(i not in s1):
                l1.append(i)

        out.append(l1)

        return out




