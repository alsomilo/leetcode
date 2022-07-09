class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort(key=lambda x: x[1])
        count = 1
        currEnd = intervals[0][1]
        
        for interval in intervals:
            if interval[0] >= currEnd:
                count+=1
                currEnd = interval[1]
                
        return len(intervals)-count
        
            