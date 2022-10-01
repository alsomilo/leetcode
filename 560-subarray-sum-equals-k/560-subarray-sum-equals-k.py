class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        preSum = [0] * (len(nums)+1)
        res = 0
        stats = {0:1}
        
        for i in range(1, len(nums)+1):
            preSum[i] = preSum[i-1]+nums[i-1]
            
        for i in range(1, len(nums)+1):
            other = preSum[i] - k 
            if other in stats:
                res += stats[other]
            
            if preSum[i] not in stats:
                stats[preSum[i]] = 0
            stats[preSum[i]] += 1
            
        
        return res