class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        
        def isValid(nums, row, col):
            
            for i in range(row):
                if abs(nums[i] - col ) == row-i or nums[i] == col:
                    return False
            return True
        
        def dfs(nums, row, path):
            
            if row == len(nums):
                res.append(path)
                return
            
            for col in range(len(nums)):
                nums[row] = col
                
                if isValid(nums, row, col):
                    tmp = '.'*len(nums)
                    dfs(nums, row+1, path + [tmp[:col]+'Q'+tmp[col+1:]])
                    
                    

        dfs([-1]*n, 0, [])
        return res