from collections import deque

class HitCounter:

    def __init__(self):
        self.hits = 0
        self.fifo = deque()
        self.size = 300
    
    def removeOld(self, timestamp):
        if timestamp > self.size:
            lastTs = timestamp - self.size + 1
            
            
            while self.fifo and self.fifo[0][0] <  lastTs:
                self.hits -= self.fifo[0][1]
                
                #debug only
                pop = self.fifo.popleft()
                print(f'pop ts = {pop[0]}, pop counts = {pop[1]}')
    

    def hit(self, timestamp: int) -> None:
        
        
        print(f'Hit: : ts = {timestamp}, lastTs = {timestamp - self.size + 1 if timestamp > self.size else 0}')
        self.removeOld(timestamp)

        

        if self.fifo and self.fifo[-1][0] == timestamp:
            self.fifo[-1][1] += 1
        else:
            self.fifo.append([timestamp, 1])
        
        self.hits += 1
        #self.lastTs = timestamp

        

    def getHits(self, timestamp: int) -> int:
        print(f'getHits: ts = {timestamp}, lastTs = {timestamp - self.size + 1 if timestamp > self.size else 0}')
        self.removeOld(timestamp)
        
        return self.hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)