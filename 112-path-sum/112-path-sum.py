# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(root, pathSum):
            
            currSum = pathSum + root.val
            left,right = False, False
            
            if not root.left and not root.right:
                return  currSum == targetSum
            
            if root.left:
                left = dfs(root.left, currSum)
                
            if root.right:
                right = dfs(root.right, currSum)
                
            
            return left or right
        
        if not root:
            return False
        
        return dfs(root, 0)
                