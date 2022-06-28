# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        '''
        self.maxLen = 0
        
        def dfs(root):
            
            if not root.left and not root.right:
                return 0, root.val
            
            left = right = 0
            
            if root.left:
                left = 1 + dfs(root.left)[0] if dfs(root.left)[1] == root.val else 0
            
            if root.right:
                right = 1 + dfs(root.right)[0] if dfs(root.right)[1] == root.val else 0
                
            
            #print(f'val is {root.val}, left = {left}, right = {right}')
            self.maxLen = max(self.maxLen, left+right)
            
            return max(left, right), root.val
        
        
        if not root:
            return 0
        
        
        dfs(root)
        
        return self.maxLen
        '''
        
        self.maxLen = 0
        
        def dfs(root, parentVal):
            
            if not root:
                return 0

            
            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)
            
            self.maxLen = max(self.maxLen, left+right)
            

            return 1+ max(left, right) if root.val == parentVal else 0
        
        if not root:
            return 0
        
        dfs(root, root.val)
        
        return self.maxLen