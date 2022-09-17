class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        if k % len(nums) == 0:
            return
        
        k %= len(nums)
        #print(nums[-k:] + nums[:-k])
        numsC = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = numsC[i]
            
        '''

        if k % len(nums) == 0:
            return
        
        k %= len(nums)

        count = 0
        start = 0
        
        
        while count < len(nums):
            
            i = start
            prev = nums[start]
        
            while True:
                newIdx = (i+k) % len(nums)

                temp = nums[newIdx]
                nums[newIdx] = prev
                prev = temp
                i = newIdx
                count += 1

                if i == start:
                    break
                
            start += 1
        


        
        