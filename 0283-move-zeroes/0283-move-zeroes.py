class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #move 0 to the end of the array, means set all non-zeros values to the head of the array, and fill all remaining items to be 0. 
        #Use two pointers to solve this problem:
        #   i to keep track of the non-zero positions at the head, 
        #   j to skip all 0s and find the next non-zero to copy its value to the i (i.e. nums[i] = nums[j] when j is still in valid range and nums[j] != 0, and then after that increment both i,j by 1)
        #   after moving non-zeros to head first, fill rest of array with 0, starting from i
        
        
        i,j = 0,0
        
        while j < len(nums):
            
            #j to skip all 0s and find the next non-zero 
            while j < len(nums) and nums[j] == 0:
                 j+=1
            
            #j exited from above loop, now j is either 1) out of bound, or 2) j is not out of bound and nums[j] is non zero (which is the one we want to find),
            
            # copy the value only if j is not out of bound (i.e. 2) above)
            if j < len(nums):
                nums[i] = nums[j]
                
                #then after that increment both i,j by 1
                i,j = i+1, j+1
        
        #   after moving non-zeros to head first, fill rest of array with 0, starting from i
        while i < len(nums):
            nums[i] = 0
            i+= 1