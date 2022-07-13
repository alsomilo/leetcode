class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo,hi = 0,len(nums)-1
        
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums)-1
        
        while lo < hi:
            mid = (lo+hi)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[hi]:    #the mid point can possibily the final anwser, hence new hi must still test mid, not mid-1
                hi = mid
            else:
                lo = mid+1 #nums[mid] > nums[hi], mid CAN NOT be the final anwser, hence exclude it from next search by, lo = mid + 1, not mid
            
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            
        
        if nums[lo] == target:
            return lo

        
        if nums[-1] > target:
            
            lo,hi = lo+1, len(nums)-2
            
            while lo <= hi:
                mid = (lo+hi)//2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid-1
                else:
                    lo = mid+1
                    
            return -1
        else:
            
            lo,hi = 1, lo-1
            
            while lo <= hi:
                mid = (lo+hi)//2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid-1
                else:
                    lo = mid+1
                    
            return -1
        