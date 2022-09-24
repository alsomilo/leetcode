class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        '''
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            
            mid = (lo+hi)//2
            
            if (mid == 0 or nums[mid-1] < nums[mid])  and (mid == len(nums)-1 or nums[mid+1] < nums[mid]):
                return mid
            
            elif mid > 0 and nums[mid-1] > nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
                
        return lo
        '''
        lo, hi = 0, len(nums)-1
        
        while lo < hi:
            
            mid = (lo+hi)//2
            
            if  nums[mid-1] < nums[mid]> nums[mid+1]:
                return mid
            
            elif nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid+1
                
        return lo
        