class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        self.res = float('Inf')
        #memo = {}
        
        def dfs(amount, count):
            
            for coin in coins:
                #print(f'amout = {amount}, coin = {coin}')
                if amount - coin == 0:
                    self.res = min(self.res, count+1)
                    #print(f'self.res={self.res}, count now = {count}')
                    return
                if amount - coin < 0:
                    return
                dfs(amount-coin, count+1)
                    
        if amount == 0:
            return 0
        
        dfs(amount, 0)
        return self.res if self.res != float('Inf') else -1
        '''
        self.res = float('Inf')
        memo = {}
        
        def dfs(amount):
            
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            res = float('Inf')
            for coin in coins:

                count = dfs(amount-coin)
                if count == -1:
                    continue
                
                res = min(res, count+1)
                
            memo[amount] = res if res != float('Inf') else -1
            return memo[amount]
        
        
        return dfs(amount)
        