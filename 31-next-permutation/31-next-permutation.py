class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #ref: https://www.youtube.com/watch?v=quAS1iydq7U&ab_channel=BackToBackSWE
        
        i = len(nums)-1
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        k = i-1
        i = len(nums)-1
        while nums[i] <= nums[k]:
            i -= 1
            
        nums[i],nums[k] = nums[k],nums[i]
        i,j=k+1,len(nums)-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        