# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #'''
        def dfs(root, pathSum):
            
            if not root:
                return False
            
            currSum = pathSum + root.val
            
            if not root.left and not root.right:
                return currSum == targetSum
            
            return dfs(root.left, currSum) or dfs(root.right, currSum)
        
        
        return dfs(root, 0)
        #'''
        
        
        '''Get min path Sum
        def dfs(root, pathSum):
            if not root.left and not root.right:
                return pathSum + root.val
            

            left, right = float('Inf'), float('Inf')
            
            if root.left:
                left = dfs(root.left, pathSum + root.val)
                
            if root.right:
                right = dfs(root.right, pathSum + root.val)
                
                
            return min(left, right)
            
        
        print(dfs(root, 0))
        return dfs(root, 0)
        '''