class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        
        stack = [asteroids[0]]
        
        for i in range(1, len(asteroids)):
            
            if stack and stack[-1] * asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                '''
                if abs(stack[-1]) > abs(asteroids[i]):
                    continue
                '''
                if stack and stack[-1] < 0:
                    stack.append(asteroids[i])
                    continue
                
                    
                if stack and abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    continue
                
                    
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroids[i]) :
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
                
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    
                    
        return stack
        