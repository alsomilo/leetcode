class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        numSet = set(nums)
        best = 0
        
        for x in numSet:
            if x-1 not in numSet:
                y = x+1
                while y in numSet:
                    y+=1
                    
                best = max(best, y-x)
        
        return best