class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        maxLen = 0
        stat = {0:-1}
        currSum = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                currSum -= 1
            else:
                currSum += 1
                
            if currSum in stat:
                maxLen = max(maxLen, i - stat[currSum])
            else:
                stat[currSum] = i
        
        return maxLen