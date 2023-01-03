class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums)-1
        res = []
        
        while i <= j:
            
            if abs(nums[i]) < abs(nums[j]):
                res = [nums[j] * nums[j]] + res
                j-=1
            else:
                res = [nums[i] * nums[i]] + res
                i+=1
                
        return res