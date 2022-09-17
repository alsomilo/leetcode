class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[timestamp, value]]
        else:
            self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.map:
            return ""
        
        lut = self.map[key]
        if len(lut) == 1:
            return lut[0][1]
        
        lo,hi = 0,len(lut)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if lut[mid][0] == timestamp:
                return lut[mid][1]
            elif lut[mid][0] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
                
        
        return lut[hi][1] if hi >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)