class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        
        intervals.sort(key=lambda interval: interval[0])
        #print(intervals)
        i,j=0,1
        res = []
        size = len(intervals)
        
        while i < size:
            lo = intervals[i][0]
            hi = intervals[i][1]
            while i < size and j < size and lo <= intervals[j][1] and hi >= intervals[j][0]:
                hi = max(hi, intervals[j][1])
                i += 1
                j += 1
                
            res.append([lo,hi])
            
            i += 1
            j += 1
            #print(f'i={i}, j={j}')
        
        return res
                