class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        nums = [i for i in range(1,n+1)]
        res = []

        def dfs(start, path):
            
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start, n):
                dfs(i+1, path + [nums[i]])
                
        dfs(0, [])
        return res
        
        
        '''
        
        nums = [i for i in range(1,n+1)]
        
        res = []
        path = []
        #print(nums)
        
        def dfs(start):
            
            if len(path) == k:
                #print(f'len of path is {len(path)}')
                res.append(path[:])
                return
            
            for i in range(start, n):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
                

        dfs(0)
        return res
        
        '''
        
        '''
        nums = [i for i in range(1,n+1)]
        
        
        def dfs(nums, path, res):
            
            if len(path) == k:
                res.append(path)
            
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], res)
                
        res = []
        dfs(nums,[],res)
        return res
        '''