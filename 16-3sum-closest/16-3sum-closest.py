class Solution:
    
    '''
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


            

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minAbs = float('Inf')
        i = 0
        nums.sort()
        
        def twoSum(left, twoSumtarget):

            lo,hi = left,len(nums)-1
            minRes = float('Inf')

            while lo < hi:
                left, right = nums[lo], nums[hi]
                currSum = left + right

                if abs(twoSumtarget - currSum) < abs(minRes):
                    minRes = twoSumtarget - currSum

                if currSum < twoSumtarget:
                    lo += 1
                else:
                    hi -= 1

            return twoSumtarget - minRes
    

        while i < len(nums)-2:
            threeSum = nums[i] + twoSum(i+1, target - nums[i])

            if abs(target - threeSum) < abs(minAbs):
                minAbs = target - threeSum
            i+=1

        return target-minAbs
                
        