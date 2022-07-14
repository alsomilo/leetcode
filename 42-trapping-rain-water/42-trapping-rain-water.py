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