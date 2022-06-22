# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def dfs(root):
            if not root:
                return
            
            if root:
                if not root.left:
                    if root.val > val:
                        root.left = TreeNode(val)
                if not root.right:
                    if root.val < val:
                        root.right = TreeNode(val)

            
            if root.val < val:
                dfs(root.right)
            else:
                dfs(root.left)
             
        if not root:
            return TreeNode(val)
        
        dfs(root)
        return root
                