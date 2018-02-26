import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

class countPrimeSetBits 
{
    public static Set<Integer> prime_set = new HashSet<Integer>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29));
    
    public static int getNumBits(int num)
    {
        int bitCount = 0;
        
        while(num > 0)
        {
          bitCount++;
          num &= (num-1);
        }
        
        return bitCount;
    }
    
    public static boolean isPrime(int num)
    {  
        return prime_set.contains(num);
    }
    
    
    public static int countPrimeSetBits_new(int L, int R) 
    {
        int num_bits = 0, prime_cnt = 0;
            
        for(int i= L; i<=R; i++)
        {
            num_bits = getNumBits(i);
            prime_cnt += isPrime(num_bits)? 1:0;
        }
        
        return prime_cnt;
    }
    
    
    public static void main(String[] args)
	{
        int num1 = Integer.parseInt(args[0]), num2 = Integer.parseInt(args[1]);
		System.out.println( "There are " + countPrimeSetBits_new(num1, num2) + " numbers between " + num1 + " and " + num2 + " , which has prime num of bits set");
	}
}
