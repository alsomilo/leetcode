class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        '''
        def isStrValid(s):
            
            stat = {'T':0, 'F':0}
            
            for c in s:
                stat[c] += 1
                
            smaller = min(stat.values())
            return smaller <= k
        
        
        def winExam(maxLen):
            
            for i in range(len(answerKey)+1 - maxLen):
                if isStrValid(answerKey[i:i+maxLen]):
                    return True
            return False
            
        
        lo,hi = 1,len(answerKey)
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if winExam(mid):
                lo = mid + 1
            else:
                hi = mid - 1
                
        return hi if hi > 0 else 1
        '''        
        
        def isStrValid(s):
            
            stat = {'T':0, 'F':0}
            
            for c in s:
                stat[c] += 1
                
            smaller = min(stat.values())
            return smaller <= k
        
        
        def winExam(maxLen):
            
            stat = {'T':0, 'F':0}
            #smaller = 0
           
            
            
            #smaller = min(stat.values())
            
            for i in range(len(answerKey)+1 - maxLen):
                
                if i == 0:
                    for c in answerKey[:maxLen]:
                        stat[c] += 1
                    #smaller = min(stat.values())

                else:
                    stat[answerKey[i-1]]-=1
                    stat[answerKey[i-1+maxLen]]+=1
                    
                    #smaller = min(smaller , min(stat.values()))
                    
                
                if min(stat.values()) <= k:
                    return True
            return False
            
        
        lo,hi = 1,len(answerKey)
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if winExam(mid):
                lo = mid + 1
            else:
                hi = mid - 1
                
        return hi if hi > 0 else 1