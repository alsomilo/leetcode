# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        def getMinNode(curr):
                    
            while curr and curr.left:
                curr = curr.left
            
            return curr
        
        def dfs(root, target):
            if not root:
                return root
           
            if root.val > target.val: 
                successor = dfs(root.left, target)
                
                if not successor:
                    return root
            elif root.val < target.val:
                successor = dfs(root.right, target)
            if root.val == target.val:
                successor = getMinNode(root.right)
            
            return successor
        return dfs(root, p)
            


            
        