class Solution:
    def simplifyPath(self, path: str) -> str:
        
        parts = path.split('/')
        #print(parts)
        
        stack = []
        res = ''
        
        for part in parts:
            
            if part == '' or part == '.':
                continue
            
            if part == '..':
                if stack:
                    stack.pop()
                continue
            
            stack.append(part)
            
            
        for item in stack:
            #res = '/'+item+res
            res += '/'+item
            
        return res if stack else '/'
            
                    
                