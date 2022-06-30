# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        self.maxSum = -1001
        
        def dfs(root):
            
            if not root:
                return 0
            
            
            ##if one of the branch sum is < 0, we can ignore/drop this branch's sum 
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            self.maxSum = max(self.maxSum, left+right+root.val) 
            
            return max(left,right) + root.val
        
        
        dfs(root)
        return self.maxSum