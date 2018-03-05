class rangeBitwiseAnd 
{
    public static int rangeBitwiseAnd_new(int m, int n)  
    {
        int result = 0, i = 0, mask = 0, old_m = 0;
        
        if(m == 0 || n == 0)
        {
            result = 0;
        }
        else if (m == n)
        {
            return m;
        }
        else
        {
            old_m = m;
            
            while(m != n)
            {               
                mask |= (1 << i++);
                m>>>=1;
                n>>>=1;
            }
            
            result = (old_m & ~mask);
            
        }
        return result;
    }
    
    public static void main(String[] args)
    {
        int m = Integer.parseInt(args[0]), n = Integer.parseInt(args[1]);
        System.out.println("Bitwise AND between " + m + " and " + n + " is: " + rangeBitwiseAnd_new(m,n));
    }
}