from collections import Counter, deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        '''
        cnt = Counter(s)
        stack = deque()
        inStack = [0] * 26
        res = ''
        
        
        for c in s:
            
            cnt[c] -= 1
            
            if not inStack[ord(c) - ord('a')]:
                
                
                
                while stack and ord(stack[-1]) > ord(c) and cnt[stack[-1]] > 0:

                    inStack[ord(stack.pop()) - ord('a')] = 0  #pop it from stack, and update poped char's instack to 0 (NOT in stack anymore since poped)
                    
                    
                stack.append(c)
                inStack[ord(c) - ord('a')] = 1
                
        while stack:
            res += stack.popleft()
            
        return res
        '''
        
        '''
        cnt = Counter(s)
        stack = deque()
        seen = set()
        res = ''
        
        
        for c in s:
            
            cnt[c] -= 1
            
            if c not in seen:
                
                while stack and ord(stack[-1]) > ord(c) and cnt[stack[-1]] > 0:
                    seen.remove(stack.pop())
                    
                stack.append(c)
                seen.add(c)
                
        while stack:
            res += stack.popleft()
            
        return res
        '''
        
        #cnt = Counter(s)
        lastIdx = {c:i for i,c in enumerate(s)}
        #print(lastIdx)
        stack = deque()
        seen = set()
        res = ''
        
        
        for i,c in enumerate(s):
            
            if c not in seen:
                
                while stack and ord(stack[-1]) > ord(c) and i < lastIdx[stack[-1]]:
                    seen.remove(stack.pop())
                    
                stack.append(c)
                seen.add(c)
                
        while stack:
            res += stack.popleft()
            
        return res
        
        
        
                
                
        
        
        
        
        