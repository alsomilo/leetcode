class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        res = []
        mySet = set(nums1+nums2+nums3)
        
        #set12 = set(nums1+nums2)
        #set32 = set(nums3+nums2)
        #set31 = set(nums3+nums1)
        
        for val in mySet:
            if (val in nums1 and val in nums2) or (val in nums2 and val in nums3) or (val in nums1 and val in nums3):
                res.append(val)
                
        return res