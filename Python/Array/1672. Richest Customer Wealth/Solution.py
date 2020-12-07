class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ##logics:
            #calculate the sum of each list
            #return the max
         wealth = [sum(i) for i in accounts]   
         return max(wealth)   