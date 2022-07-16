class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        
        currMin = int(current[:2])*60 + int(current[-2:])
        targetMin = int(correct[:2])*60 + int(correct[-2:])
        #print(currMin, targetMin)
        options = [60,15,5,1]
        i=0
        res = 0
        
        while currMin < targetMin:
            
            while i < 4 and currMin + options[i] > targetMin:
                i += 1
                
            currMin += options[i]
            res += 1
            
        return res
            
        
        
        
        '''
        self.options = [60,15,5,1]
        self.memo = {}
        
        def isGreater(currTime, correct):
            if int(currTime[:2]) > int(correct[:2]):
                return True
            if int(currTime[:2]) == int(correct[:2]) and int(currTime[-2:]) > int(correct[-2:]):
                return True           
            
            return False
        
        
        def getNewTime(currTime, option):
            secInt = int(currTime[-2:]) + option
                
            minInc = secInt//60
            newSec = secInt % 60
                
            newMin = minInc + int(currTime[:2])
            newMin %= 24

            return ('0' if int(newMin)<10 else '') + str(newMin) + ':' + ('0' if int(newSec)<10 else '') + str(newSec)
                
            
                
        
        
        def dfs(currTime):
            #print(f'{currTime}, {correct}')
            if currTime == correct:
                #print(f'Now equal!')
                return 0
            if isGreater(currTime, correct):
                #print(f'grater!!')
                return -1
            if currTime in self.memo:
                return self.memo[currTime]
            
            minTimes = float('Inf')
            
            for option in self.options:
                timesNeeded = dfs(getNewTime(currTime, option))
                
                if timesNeeded == -1:
                    continue
                   
                minTimes = min(minTimes, timesNeeded+1)
                    
            self.memo[currTime] = minTimes if minTimes != float('Inf') else -1        
            return self.memo[currTime]
                
        return dfs(current)
        
        
        #print(isGreater("09:45","06:45"))
        '''