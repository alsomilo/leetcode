# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        self.accum = 0
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.right)
            
            self.accum += root.val
            root.val = self.accum
            dfs(root.left)
            
        dfs(root)
        return root
        