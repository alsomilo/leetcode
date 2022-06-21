# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.currSum = 0 
        def dfs(root):
            if not root:
                return
            
            
            dfs(root.right)
            self.currSum += root.val
            
            root.val = self.currSum
            
            dfs(root.left)
            
        dfs(root)
        return root
            
            
