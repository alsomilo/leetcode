class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ''' two pointers
        i,j = 0,len(nums)-1
        res = []
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                res = [nums[j] ** 2] + res
                j-=1
            else:
                res = [nums[i] ** 2] + res
                i+=1
        
        return res
        '''
        
        res = [num**2 for num in nums]
        res.sort()
        return res