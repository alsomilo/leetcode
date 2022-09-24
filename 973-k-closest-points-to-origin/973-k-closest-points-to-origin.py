class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            
            x,y = point[0],point[1]
            
            return point, x**2 +y**2
        
        
        dis = [getDistance(point) for point in points]
        
        dis.sort(key = lambda x: x[1])
        res = [x[0] for x in dis]
        return res[:k]