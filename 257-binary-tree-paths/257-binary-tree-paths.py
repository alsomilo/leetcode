# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        
        def dfs(root, pathStr):
            
            currStr = pathStr + str(root.val)
            
            if not root.left and not root.right:
                res.append(currStr)
                
            if root.left:
                dfs(root.left, currStr + '->')
                
            if root.right:
                dfs(root.right, currStr + '->')
                
                
        dfs(root, '')
        return res
            
            
        