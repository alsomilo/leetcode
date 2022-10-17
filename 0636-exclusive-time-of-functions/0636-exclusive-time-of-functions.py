class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # use a stack to track the actual call stack, by pusing the fn id into stack at "start", and pop fn id at "end", 
        # since we only push func id into stack, we use an extra var prev_startTime to track the most recent START time
        # 1) during push at a "start":
        #   we add the run time accumulated so far to result of the last started func id (which can be retreived from stack top stack[-1], since both prev_startTime and ts are start time, the accumulated add value is ts -           prev_startTime ), 
        #   and we push the current start fc id into the stack and update the prev_startTime to the current start ts
        
        # 2) during pop at a "end":
        #  we pop the top of the stack, which will get the ended func id, and add the accumulated run time to the result of the that ended func id, since the ts in this condition is the end time, we need to make sure the 
        #  the added accumulated run time is the new start time - old start time, new start time will be current ts+1, so we do += ts+1- prev_startTime, and update prev_startTime to be new start time of ts (current end time)+1
        
        stack = []
        res = [0] * n
        prev_startTime = 0
        
        for log in logs:
            fn, fnType, ts = log.split(':')
            fn, ts = int(fn), int(ts)
            
            if fnType == "start":
                # 1) during push at a "start":
                #   we add the run time accumulated so far to result of the last started func id (which can be retreived from stack top stack[-1], since both prev_startTime and ts are start time, the accumulated add value is ts -                           prev_startTime ), 
                if stack:
                    res[stack[-1]] += ts - prev_startTime
                
                #   after that, we push the current start fc id into the stack and update the prev_startTime to the current start ts
                stack.append(fn)
                prev_startTime = ts
                
            else:
                
                 # 2) during pop at a "end":
                     #  we pop the top of the stack, which will get the ended func id, and add the accumulated run time to the result of the that ended func id, since the ts in this condition is the end time, we need to make sure the 
                     #  the added accumulated run time is the new start time - old start time, new start time will be current ts+1, so we do += ts+1- prev_startTime, (ts+1 is the new start time)
                    
                res[stack.pop()] += ts+1 - prev_startTime
                
                # update prev_startTime to be new start time of ts (current end time) +1
                prev_startTime = ts + 1
                
        return res
                