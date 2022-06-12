class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        res = []
        nums.sort()
        
        def dfs(nums, path, res):
            
            if not nums:
                res.append(path)
                return 
            

            
            prevNum = -101
            for i in range(len(nums)):
                
                if prevNum != nums[i]:    #cut branch logic: avoid processing branch for the node which has same value with prevNum  
                    prevNum = nums[i]
                    dfs( nums[:i]+nums[i+1:] , path + [nums[i]], res)
                
                
        dfs(nums, [], res)
        
        return res
        '''
        
        res = []
        nums.sort()
        
        def dfs(nums, path, res):
            
            if not nums:
                res.append(path)
                return 
            

            for i in range(len(nums)):
                
                if not (i > 0 and nums[i-1] == nums[i]):    #cut branch logic: avoid processing branch for the node which has same value with prevNum  
                    #prevNum = nums[i]
                    dfs( nums[:i]+nums[i+1:] , path + [nums[i]], res)
                
                
        dfs(nums, [], res)
        
        return res