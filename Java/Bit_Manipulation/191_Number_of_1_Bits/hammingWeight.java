public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) 
    {       
        int count = 0;
        
        if(n!=0)
        {
            for(count = 1; (n&=(n-1)) != 0; count++)
            {
                //do nothing
            }
        }
            
        return count;
    }
}
