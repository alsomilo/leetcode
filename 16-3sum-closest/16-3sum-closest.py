class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        
        def twoSum(left, twoSumtarget):
            
            lo,hi = left,len(nums)-1
            minRes = float('Inf')
            
            while lo < hi:
                left, right = nums[lo], nums[hi]
                currSum = left + right
                
                if abs(currSum - twoSumtarget) < abs(minRes):
                    minRes = currSum - twoSumtarget
                    
                if currSum < twoSumtarget:
                    lo += 1
                else:
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

            i+=1
            
        return target-minAbs
                    
                