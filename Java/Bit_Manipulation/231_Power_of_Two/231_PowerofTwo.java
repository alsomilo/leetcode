class Solution {
    public static boolean isPowerOfTwo(int n) 
    {
        
        if(n <= 0)
        {
            return false;            
        }    
        else
        {
            return ((n & (n-1)) == 0);
        }
        
    }
    
    public static void main(String[] args)
    {
        int n = 16; 
        System.out.println(n + " is a power of 2? " + isPowerOfTwo(n));
    }
}