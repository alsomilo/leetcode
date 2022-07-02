class Solution:
    def reverse(self, x: int) -> int:
        
        minVal = ((-1) * (1 << 31))
        maxVal = ((1 << 31)-1)
        #print(minVal, maxVal)
        
        xCopy = x
        x = abs(x)
        res = 0
        
        while x:
            res = res*10 + x % 10
            x //= 10
        #print(res)
        res = res * (-1) if xCopy < 0 else res
        return res if (minVal <= res <= maxVal) else 0
            
        
            