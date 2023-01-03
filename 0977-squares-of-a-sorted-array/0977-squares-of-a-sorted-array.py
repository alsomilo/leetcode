class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        #two pointers
        
        #method 1: use two pointers: since the original input array is already sorted, the min value is at most left, and max value at most right. 
        # contine the while loop as long as i <= j, pls note we need the <= here , not <. because when i ==j, the value still need to be squred and saved into target array
        # for each iteration, check which abs value is bigger, and save the bigger one's squred value from right to left (append value to the left of the res array) and move the i or j accordingly 
        
        '''
        i,j = 0,len(nums)-1
        res = []
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                res = [nums[j] ** 2] + res
                j-=1
            else:
                res = [nums[i] ** 2] + res
                i+=1
        
        return res
        '''
        #'''
        #method 2:  directly generated new squared array first, and then sort
        res = [num**2 for num in nums]
        res.sort()
        return res
        #'''