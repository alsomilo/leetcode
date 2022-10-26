from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(), Lock(), Lock())
        self.locks[0].acquire() #even
        self.locks[1].acquire() #odd
        self.i = 0
        
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.locks[2].acquire()
            printNumber(0)
            self.i+=1
            self.locks[self.i % 2].release()   #release odd lock

        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n//2):
            self.locks[0].acquire()
            printNumber(self.i)
            self.locks[2].release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n+1)//2):
            self.locks[1].acquire()
            printNumber(self.i)
            self.locks[2].release()