class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        #given the majority element are more than half of the array, that means if we sort the array and return the middle one, it will be the majority element
        
        nums.sort()
        return nums[len(nums)//2]