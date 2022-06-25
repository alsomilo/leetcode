# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        if not root:
            return []
        
        fifo = deque()
        fifo.append(root)
        res = []
        
        while fifo:
            
            currLen = len(fifo)
            
            for i in range(currLen):
                currNode = fifo.popleft()
                
                
                if i == currLen - 1:
                    res.append(currNode.val)
        
                if currNode.left:
                    fifo.append(currNode.left)
                    
                if currNode.right:   
                    fifo.append(currNode.right)
                    
        
        return res
        
        '''
        
        
        def dfs(root):
            if not root:
                return []
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return [root.val] + right + left[len(right):]
        
        
        return dfs(root)