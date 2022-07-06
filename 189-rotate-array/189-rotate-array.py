class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k % len(nums) == 0:
            return
        
        k %= len(nums)
        #print(nums[-k:] + nums[:-k])
        numsC = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = numsC[i]
        
        