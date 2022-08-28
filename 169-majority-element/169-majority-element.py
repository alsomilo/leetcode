class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        numLen = len(nums)
        
        return nums[numLen//2] if numLen % 2 == 1 else nums[numLen//2-1]
        