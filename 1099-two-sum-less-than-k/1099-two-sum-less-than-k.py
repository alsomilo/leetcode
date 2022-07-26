class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        
        nums.sort()
        lo,hi = 0,len(nums)-1
        res=0
        
        while lo < hi:
            left,right = nums[lo],nums[hi]
            currSum = left + right

            if currSum < k:
                res = max(res, currSum)
                while lo < hi and left == nums[lo]:
                    lo += 1
            else:
                while lo < hi and right == nums[hi]:
                    hi -= 1
                    
        return res if res != 0 else -1
        
            
            