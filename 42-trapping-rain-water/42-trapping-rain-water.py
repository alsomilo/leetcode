class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        '''brutal force
        res = 0
                
        for i in range(0, len(height)):
            
            leftMax = rightMax = 0
            for x in range(i+1):
                leftMax = max(leftMax, height[x])
                
            for y in range(i, len(height)):
                rightMax = max(rightMax, height[y])
                
            #water = min(leftMax, rightMax) - height[i]
            res += min(leftMax, rightMax) - height[i]
            #print(f'i = {i}, leftMax = {leftMax}, rightMax = {rightMax}, res={res}')
        return res
        '''
        
        '''memo
        leftMax = [height[0]]*len(height)
        rightMax = [height[-1]]*len(height)
        
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
            
        for i in range(len(height)-2, -1,-1):
            rightMax[i] = max(rightMax[i+1], height[i])
            
        #print(leftMax)
        #print(rightMax)
        
        res = 0
        
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i])-height[i]
            
        return res
        '''
        
        
        left, right = 0, len(height)-1
        res = 0
        leftMax = rightMax = 0
        
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            
            #res += min(leftMax, rightMax) - height[left] if leftMax < rightMax else height[right]
            
            if leftMax < rightMax:
                res += leftMax - height[left]
                left += 1
            else:
                res += rightMax - height[right]
                right -= 1
                
        return res