class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #'''
        res = []
        
        def dfs(start, path, combSum):
            
            if combSum == target:
                res.append(path)
            if combSum > target:
                return
            
            for i in range(start, len(candidates)):
                dfs(i, path+[candidates[i]], combSum + candidates[i])
                
        dfs(0, [], 0)
        return res
        #'''
        '''
        res = []
        
        def dfs(candidates, path, combSum):
            
            if combSum == target:
                res.append(path)
            if combSum > target:
                return
            
            for i in range(len(candidates)):
                dfs(candidates[i:], path+[candidates[i]], combSum + candidates[i])
                
        dfs(candidates, [], 0)
        return res
        '''