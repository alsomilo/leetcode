class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i, v in enumerate(nums):
            other = target - v
            
            if other in seen:
                return [seen[other], i]
            
            seen[v] = i
            #print(f'save seen[{other}] = {i}')
            
            