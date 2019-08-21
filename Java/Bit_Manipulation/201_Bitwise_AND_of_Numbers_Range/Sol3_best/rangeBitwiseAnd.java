/*
LC-201

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

*/

//idea: shift M and N until they are equal, then result will be M << i (i is the shift times)

class rangeBitwiseAnd 
{
    public static int rangeBitwiseAnd_new(int m, int n)  
    {   
	    int i;
		
        if(m == 0 || n == 0)
        {
            return 0;
        }
        else if (m == n)
        {
            return m;
        }
        else
        {
			for(i=0; m != n; i++)
			{
				m >>>= 1;
				n >>>= 1;
			}
        }
        return m << i;
    }
    
    public static void main(String[] args)
    {
        int m = Integer.parseInt(args[0]), n = Integer.parseInt(args[1]);
        System.out.println("Bitwise AND between " + m + " and " + n + " is: " + rangeBitwiseAnd_new(m,n));
    }
}