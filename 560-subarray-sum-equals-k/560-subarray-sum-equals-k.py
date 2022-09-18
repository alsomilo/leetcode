class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #use prefix sum, subarray sum equal to k ==> preSum[i] - preSum[prev] == k, prev here means previous index
        preSum = [0] * (len(nums)+1)
        res = 0
        
        #use a stats here to main the count of each preSum value
        stats = {0:1}
        
        #calc the preSum array
        for i in range(1, len(nums)+1):
            preSum[i] = preSum[i-1]+nums[i-1]
            
        for i in range(1, len(nums)+1):
            other = preSum[i] - k 
            if other in stats:
                res += stats[other]
            
            #count the preSum count, please note that same preSum value can corresponds to different array index, hence different subarray. Since this problem 
            #does not ask for listing all subarrays, just find out the count, so we use a counter to maintain the count of one pariticular preSum, and accumulate
            # the res tarwads the total counts
            if preSum[i] not in stats:
                stats[preSum[i]] = 0
            stats[preSum[i]] += 1
            
        
        return res
        
        
        '''
        #This approach is not what the problem asked, but it extends the problem by listing all subarray, which will exceed mem limit for very long nums
        # this approach is just to show all qualified subarray with sum equal to k
        preSum = [0] * (len(nums)+1)
        res = []
        stats = {0:[0]}
        
        for i in range(1, len(nums)+1):
            preSum[i] = preSum[i-1]+nums[i-1]
            
        for i in range(1, len(nums)+1):
            other = preSum[i] - k 
            if other in stats:
                for idx in stats[other]:
                    res.append(nums[idx: i])
            
            if preSum[i] not in stats:
                stats[preSum[i]] = []
            stats[preSum[i]].append(i)
            
        print(res)
        return len(res)
        '''
        