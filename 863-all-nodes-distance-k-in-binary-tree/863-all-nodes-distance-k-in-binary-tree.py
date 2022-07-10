# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parent = {}
        fifo = deque()
        visited = set()
        res = []
        distance = 0
        
        def dfs(root, parentNode):
            if not root:
                return
            
            parent[root.val] = parentNode
            dfs(root.left, root)
            dfs(root.right, root)
            
        
        dfs(root, None)
        
        fifo.append(target)
        visited.add(target.val)
        
        
        while fifo:
            currLen = len(fifo)
            
            for i in range(currLen):
                currNode = fifo.popleft()
                
                if distance > k:
                    break
                
                if distance == k:
                    res.append(currNode.val)
                    
                if parent[currNode.val] and parent[currNode.val].val not in visited:
                    visited.add(parent[currNode.val].val)
                    fifo.append(parent[currNode.val])
                    
                if currNode.left and currNode.left.val not in visited:
                    visited.add(currNode.left.val)
                    fifo.append(currNode.left)
                    
                if currNode.right and currNode.right.val not in visited:
                    visited.add(currNode.right.val)
                    fifo.append(currNode.right)
                    
            
            distance += 1
            
        return res
        
        
        