class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        ''' Do not use, time limit exceed!!!
        #tank = 0
        length = len(gas)
        
        for i in range(length):
            failed = False
            tank = 0
            for j in range(i, i+length):
                tank += gas[j % length]
                tank -= cost[j % length]
                
                #print(f'i={i}, j={j}, tank={tank}')
                if tank < 0:
                    failed = True
                    break
                    
            if not failed:
                return i
            
        return -1
        '''
        
        #'''
        
        #first, calculate the net gain of gas at each station.
        #since gas in the tank can be carried over to the next station, so this trigger the thought of prefixSum!! which also aggregate previous element's sum
        
        
        #if starting from the lowest point in prefixSum and travel entire array, this make a new prefixSum array based on the new net[], if the new prefixSum array's lowest point is > 0, thenwe can travel around
        
        
        
        
        
        #first, calculate the net gain of gas at each station.
        net = [gas[i] - cost[i] for i in range(len(gas))]
        print(net)
        
        #since gas in the tank can be carried over to the next station, so this trigger the thought of prefixSum!! which also aggregate previous element's sum
        preSum = [0]
        for i in range(len(gas)):
            preSum.append(net[i]+preSum[-1])
            
        print(preSum)
        print(min(preSum))
        print(preSum.index(min(preSum)))
        
        #if starting from the lowest point in prefixSum and travel entire array, this make a new prefixSum array based on the new net[], if the new prefixSum array's lowest point is > 0, thenwe can travel around
        start = preSum.index(min(preSum))   #find out the lowest point index in the current prefixSum array
        newNet = net[start:]+net[:start]    #start from this lowest pint index , and creat new net[]
        print(newNet)
        
        preSum = [0]
        for i in range(len(gas)):
            preSum.append(newNet[i]+preSum[-1])
        
        print(preSum)
        if min(preSum) < 0:
            return -1
        return start
        #'''