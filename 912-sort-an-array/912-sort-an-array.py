class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        '''
        def quicksort(nums):
            length = len(nums)
            if length == 0 or length == 1:
                return nums
            
            mid = length//2
            

            #left = [x for i,x in enumerate(nums) if i !=mid and  x < nums[mid]]
            #right = [x for i,x in enumerate(nums) if i !=mid and  x >= nums[mid]]


            left = []
            right = []
            for i,num in enumerate(nums):
                if i != mid:
                    if num < nums[mid]:
                        left.append(num)
                    else:
                        right.append(num)
       
            return quicksort(left) + [nums[mid]] + quicksort(right)
        
        return quicksort(nums)
        '''
        
        
        def mergeSort(nums):
            if len(nums) == 0 or len(nums) == 1:
                return nums
            
                        
            mid = len(nums)//2
            
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            i=j=0
            ret = []
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ret.append(left[i])
                    i+=1
                else:
                    ret.append(right[j])
                    j+=1
                
            ret += left[i:] if i < len(left) else right[j:]
            return ret
        
        return mergeSort(nums)
                
                    
            
            