class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        '''
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
        net = [gas[i] - cost[i] for i in range(len(gas))]
        print(net)
        preSum = [0]
        for i in range(len(gas)):
            preSum.append(net[i]+preSum[-1])
            
        print(preSum)
        print(min(preSum))
        print(preSum.index(min(preSum)))
        
        start = preSum.index(min(preSum))
        newNet = net[start:]+net[:start]
        print(newNet)
        
        preSum = [0]
        for i in range(len(gas)):
            preSum.append(newNet[i]+preSum[-1])
        
        print(preSum)
        if min(preSum) < 0:
            return -1
        return start
        #'''