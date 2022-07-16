class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        '''
        self.res = 0
        
        def dfs(x,y):
            
            if x == n or y == m:
                return 
            
            if x == n-1 and y == m-1:
                self.res += 1
                return
            
            dfs(x+1, y)
            dfs(x, y+1)
            
        dfs(0,0)
        
        return self.res

        
        #self.res = 0
        '''
        

        memo = {}
        
        def dfs(x,y):
            
            if x == n or y == m:
                return 0
            
            if x == n-1 and y == m-1:
                return 1
            
            
            if (x,y) in memo:
                return memo[(x,y)]
            
            '''
            if (x+1,y) in memo:
                return memo[(x+1,y)]
            if (x,y+1) in memo:
                return memo[(x,y+1)]
            '''
            
            right = dfs(x+1, y)
            memo[(x+1,y)] = right
            
            
            down = dfs(x, y+1)
            memo[(x,y+1)] = down
            
            return right + down
    
        return dfs(0,0)

        
        