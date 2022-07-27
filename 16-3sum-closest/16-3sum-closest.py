class Solution:
    
    def twoSum(self, nums, start, target):
        lo,hi = start, len(nums)-1
        
        delta = float('Inf')
        while lo < hi:
            twoSum = nums[lo] + nums[hi]
            
            if abs(delta) > abs(target-twoSum):
                delta = target-twoSum
                
            if twoSum < target:
                lo += 1
            else:
                hi -= 1
        
        return target-delta
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 3:
            return 0

        nums.sort()
        delta = float('Inf')
        i = 0
        while i < len(nums)-2:
            
            threeSum = nums[i] + self.twoSum(nums, i+1, target-nums[i])
            
            if abs(delta) > abs(target- threeSum):
                delta = target - threeSum
            i+=1
            
        return target - delta
    


        
        '''
        def twoSum(left, twoSumtarget):
            
            lo,hi = left,len(nums)-1
            minRes = float('Inf')
            
            while lo < hi:
                left, right = nums[lo], nums[hi]
                currSum = left + right
                
                if abs(currSum - twoSumtarget) < abs(minRes):
                    minRes = currSum - twoSumtarget
                    
                if currSum < twoSumtarget:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                else:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                        
            return twoSumtarget - minRes
                

            
        minAbs = float('Inf')
        i = 0
        res = 0
        nums.sort()
        
        while i < len(nums)-2:
            threeSum = nums[i] + twoSum(i+1, target - nums[i])
            
            if abs(threeSum - target) < abs(minAbs):
                minAbs = threeSum - target
                
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            i+=1
            
        return target-minAbs
        '''
                    
        