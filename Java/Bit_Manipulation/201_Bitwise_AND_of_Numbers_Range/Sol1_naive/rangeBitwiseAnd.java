class rangeBitwiseAnd 
{
    public static int rangeBitwiseAnd_new(int m, int n)  
    {
        int result = 0,  mask = 0, old_m = 0;
        
        if((m == 0 || n == 0) ||
            (Integer.numberOfLeadingZeros(m) > Integer.numberOfLeadingZeros(n)))
        {
            result = 0;
        }
        else if (m == n)
        {
            return m;
        }
        else
        {

            mask = ((Integer.highestOneBit(m ^ n) << 1) -1);
            
            old_m = m;
            m &= mask;
            n &= mask;
            
            result = m;
            
            for(int i = m+1; i <= n; i++)
            {
                result &= i;
            }
            
            result |= ( old_m & (~mask));
        }
        return result;
    }
    
    public static void main(String[] args)
    {
        int m = Integer.parseInt(args[0]), n = Integer.parseInt(args[1]);
        System.out.println("Bitwise AND between " + m + " and " + n + " is: " + rangeBitwiseAnd_new(m,n));
    }
}