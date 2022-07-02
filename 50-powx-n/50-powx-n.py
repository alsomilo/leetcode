class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #return x ** n
        
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n % 2:
            return x * self.myPow(x, n-1)
        
        return self.myPow(x*x, n//2)  # x**n => (x**2) ** (n//2), pls note that 2 * 1/2 cancel each other   