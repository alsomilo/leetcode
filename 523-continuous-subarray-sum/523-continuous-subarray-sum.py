class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        seen = {0:-1}
        currSum = 0

        
        for i,num in enumerate(nums):

            
            currSum += num
            #print(f'currSum = {currSum}')
            
            remainder = currSum % k
            
            if remainder in seen:
                
                if i > seen[remainder]+1:
                    return True
            else:
                seen[remainder] = i
                #print(f'seen[{remainder}] = {i}')
            
            
        return False