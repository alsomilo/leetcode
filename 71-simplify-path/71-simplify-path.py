class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # Top:
        # given we have '..' in the path, which will revert the most recent path, so we use a stack to do this, which can pop the most recent path pushed to the stack (to achieve the revert effct)
        
        # We first split the path into a list by using '/' as the seperator, and operate on this list
        # we need to skip the '' and '.' to ignore the trailing '/' or any '.' which indicates current directory
        # any '..' require to pop the stack , if the stack is non empty. If stack is already empty, no need to do anything since going further UP from root / takes no effect (i.e. still at root)
        
        # if no above condition met, then we can push this current part into the stack
        
        # finally we pop the stack and append to the left of the res, since stack's top has the most recent directory, and stack bottom s the directory directly under root
        # if res is still empty string '', that means stack was empty before which indicates we are at root, so return only root '/' if res is emptry, otherwise return res
        
        
        
        #Code:
        
        # We first split the path into a list by using '/' as the seperator, and operate on this list
        parts = path.split('/')
        #print(parts)
        
        stack = []
        res = ''
        
        for part in parts:
            
            # we need to skip the '' and '.' to ignore the trailing '/' or any '.' which indicates current directory
            if part == '' or part == '.':
                continue
            
            # any '..' require to pop the stack , if the stack is non empty. If stack is already empty, no need to do anything since going further UP from root / takes no effect (i.e. still at root)
            if part == '..':
                if stack:
                    stack.pop()
                continue
            
            # if no above condition met, then we can push this current part into the stack
            stack.append(part)
            
        '''
        for item in stack:
            #res = '/'+item+res
            res += '/'+item
        '''    
        # finally we pop the stack and append to the left of the res, since stack's top has the most recent directory, and stack bottom s the directory directly under root
        while stack:
            res = '/'+stack.pop() + res
        
        # if res is still empty string '', that means stack was empty before which indicates we are at root, so return only root '/' if res is emptry, otherwise return res
        return res if res else '/'
            
                    
                