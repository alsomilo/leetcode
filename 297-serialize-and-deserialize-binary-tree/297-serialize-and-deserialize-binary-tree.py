# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        
        if not root:
            return '#,'
        
        mid   = str(root.val)+','
        left  = self.serialize(root.left)
        right = self.serialize(root.right)
        #print(mid+left+right)
        return mid+left+right
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        if data == '#,':
            #print(f'empty str!')
            return None
        
        
        queue = deque(data.split(','))
        #print(queue)
        
        def dfs(queue):
            if not queue:
                return None
            
            
            rootVal = queue.popleft()
            
            if rootVal == '#':
                return None
            
            root = TreeNode(int(rootVal))
            #print(queue)
            root.left = dfs(queue)
            root.right = dfs(queue)
            return root
        
        return dfs(queue)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))