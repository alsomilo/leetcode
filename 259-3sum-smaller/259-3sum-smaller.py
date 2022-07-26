class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = 0
        
        def twoSum(left, twoSumtarget):
            count = 0
            lo,hi = left,len(nums)-1
            while lo < hi:
                left,right = nums[lo],nums[hi]
                currSum = left + right

                if currSum < twoSumtarget:
                    count += (hi-lo)
                    lo += 1
                    '''
                    while lo < hi and left == nums[lo]:
                        lo += 1
                    '''
                else:
                    hi -= 1
                    '''
                    while lo < hi and right == nums[hi]:
                        hi -= 1
                    '''
            return count
        
        i=0
        while i < len(nums):
            val = twoSum(i+1, target - nums[i])
            #print(f'twoSum from {i+1}, with target {target - nums[i]} = {val}')
            res += val
            
            '''
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            '''
            
            i+=1
            
        return res
                    
        
                    
            