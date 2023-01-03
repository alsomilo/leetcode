class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        intervals.sort(key = lambda x : x[0])
        start,end = [], []
        for interval in intervals:
            start.append(interval[0]) 
            end.append(interval[1])
            
        i,j,l=0,0,len(intervals)
        
        while i < l and j < l:
            
            if abs(i-j) > 1:
                return False
            
            if start[i] < end[j]:
                i+=1
            else:
                j+=1
            
            
        return True if abs(i-j) < 2 else False