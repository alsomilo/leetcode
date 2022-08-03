class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        '''
        def overlap(rangeA, rangeB):
            if rangeA[1] > rangeB[0] and rangeA[0] < rangeB[1]:
                #print(f'{rangeA} and {rangeB} overlap!')
                return True
            #print(f'{rangeA} and {rangeB} NO overlap!')
            return False
        
        
        timeline = []
        
        for interval in intervals:
            timeline += interval
            
        timeline.sort()
        
        i = 0
        maxRoom = 1
        
        while i+1 < len(timeline):
            currRoom = 0
            
            for interval in intervals:
                if overlap(interval, [timeline[i],timeline[i+1]]):
                    currRoom += 1
            
            maxRoom = max(maxRoom, currRoom)
            
            i+=1
            
        return maxRoom
        '''
        
        
        start = [interval[0] for interval in intervals]
        end =   [interval[1] for interval in intervals]
        start.sort()
        end.sort()
        maxRoom = 0 
        curRoom = 0
        
        i,j = 0,0
        
        '''
        while i < len(start) or j < len(end):
            st = start[i] if i < len(start) else float('Inf')
            et = end[j] if j < len(end) else float('Inf')
            
            if st < et:
                curRoom += 1
                maxRoom = max(maxRoom, curRoom)
                i += 1
            else:
                curRoom -= 1
                maxRoom = max(maxRoom, curRoom)
                j += 1
        '''
        while i < len(start):
            st = start[i] 
            et = end[j]
            
            if st < et:
                curRoom += 1
                maxRoom = max(maxRoom, curRoom)
                i += 1
            else:
                curRoom -= 1
                maxRoom = max(maxRoom, curRoom)
                j += 1
        
        return maxRoom
                
            
            
            