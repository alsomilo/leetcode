# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        def dfs(root, path, prevSum):
            
            currSum = root.val + prevSum
            
            if not root.left and not root.right:
                if currSum == targetSum:
                    path.append(root.val)
                    res.append(path)
                return
            
            
            if root.left:
                dfs(root.left, path + [root.val], currSum)
                
            if root.right:
                dfs(root.right, path + [root.val], currSum)
        
        if not root:
            return []
        
        res = []        
        dfs(root, [], 0)
        return res
        
            
                
            
            