# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        self.preSum = 0
        self.stat = {}
        self.stat[0] = 1  #do not miss the 0 entry in preSum!!
        self.res = 0
        
        def dfs(root):
            if not root:
                return
            
            self.preSum += root.val
            
            self.res += self.stat.get(self.preSum - targetSum, 0)
            
            
            self.stat[self.preSum] = self.stat.get(self.preSum, 0) + 1           
            
            
            dfs(root.left)
            dfs(root.right)
            
            
            self.stat[self.preSum] -= 1
            self.preSum -= root.val
            
        dfs(root)
        
        return self.res