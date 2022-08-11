class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = list(set(sorted(nums)))
        nums.sort()
        i = 0
        oneFound = False
        print(nums)
        for num in nums:
            
            if num == 1:
                i = 2
                oneFound = True
            elif i != 0:
                if i == num:
                    i += 1
                else:
                    return i
        return i if oneFound else 1