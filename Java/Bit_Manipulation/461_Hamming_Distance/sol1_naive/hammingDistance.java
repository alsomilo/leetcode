class Solution 
{
    public int hammingDistance(int x, int y) 
    {
        int z, count = 0;
        
        z = (x ^ y);
        
        while(z)
        {
            count += (z & 0x1); 
            z >>= 1; 
        }
        
        return count;
    }
}