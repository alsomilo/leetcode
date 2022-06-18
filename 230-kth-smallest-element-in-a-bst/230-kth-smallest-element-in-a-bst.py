# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        '''
        def dfs(root):
            if not root:
                return []
            
            return dfs(root.left) + [root.val] + dfs(root.right)
        
        stack = dfs(root)
        #print(stack)
        
        return stack[k-1]
        '''
        
        self.count = 0
        self.res = 0
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            
            self.count+=1
            if self.count == k:
                self.res = root.val
            
            dfs(root.right)
            return
        
        dfs(root)

        
        return self.res
        
            
        