class Node:
    
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.size = capacity
        self.head = Node(key=-1)
        self.tail = Node(key=-2)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.map:
            ret = self.map[key].val
            if self.map[key] is not self.head.next:
                self.removeNadd(self.map[key], key, ret)
            return ret
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            if self.map[key] is self.head.next:
                self.head.next.val = value
            else:
                self.removeNadd(self.map[key], key, value)
        else:
            if len(self.map) == self.size:
                self.removeNadd(self.tail.prev, key, value)
            else:
                self.add(key,value)
                
    def add(self,key,value):
        node = Node(key,value)
        self.map[key] = node
        self.lnkLstAdd(node)
        
    def removeNadd(self,node, key , value):
        if node.key == key:
            self.map[key].val = value
        else:
            self.map.pop(node.key)
            node.key , node.val = key, value
            self.map[key] = node
        
        self.lnkLstRemove(node)
        self.lnkLstAdd(node)
        
    def lnkLstAdd(self,node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
    
    def lnkLstRemove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)