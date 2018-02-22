class Solution 
{
    public int hammingDistance(int x, int y) 
    {
        int z, count = 0;
        
        z = (x ^ y);
        

        if(z!=0)
        {
            /*there're bits position difference*/
            /*at least one bit is different*/
            count = 1;
            
            /*clear LSB each time and count*/
            while((z &= (z-1)) > 0)
            {
                count++;        
            }
        }
                
        
        return count;
    }
}