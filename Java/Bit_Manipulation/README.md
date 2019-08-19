338. Counting Bits: idea is to use O(n), means in each iteration, use just *ONE* operation to find num of bits set to 1, that means we need a *FORMULAR*, and this becomes a high school math problem :)

considering we are given the array here, that is an *INDICATION* to use previous calculated value (saved in array) to derive new value. I am pretty sure the person who came up with this question actually had the solution first, then come up with the question which intentionally use array.. The question here which intentionally introduces the array has its own purpose, so think in this way...

          /* array[i] = array[i/2] + i%2*/
          /* /2 means >> 1, similarly, /4 means >> 2, /8 means >> 3, /n means >>log(n)
             %2 means &1, similarly , %4 means &3, %8 means &7, so %n means &(n-1)*/ 
			 
			 test
