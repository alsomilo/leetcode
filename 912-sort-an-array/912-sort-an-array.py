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
        '''         
        
        temp = nums[:]
        
        def mergeSort(nums, start, end):
            
            if start == end:
                return
            
            
            mid = (start+end)//2
            
            mergeSort(nums, start, mid)
            mergeSort(nums, mid+1, end)
            
            for i in range(start, end+1):
                temp[i] = nums[i]
             
            i,j,p = start, mid+1, start
            
            while p <= end:
                if i == mid+1:
                    nums[p] = temp[j]
                    j+=1
                elif j == end+1:
                    nums[p] = temp[i]
                    i+=1
                    
                elif temp[i] < temp[j]:
                    nums[p] = temp[i]
                    i+=1
                else:
                    nums[p] = temp[j]
                    j+=1
                
                p+=1

        
        mergeSort(nums, 0 , len(nums)-1)
        return nums
            
            