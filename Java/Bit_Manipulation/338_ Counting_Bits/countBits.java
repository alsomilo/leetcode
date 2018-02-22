class Solution 
{
    public int[] countBits(int num) 
    {
        int[] array = new int[num+1];
        for(int i=1; i<=num; i++)
        {
          /* array[i] = array[i/2] + i%2*/
          /* /2 means >> 1, similarly, /4 means >> 2, /8 means >> 3, /n means >>log(n)
             %2 means &1, similarly , %4 means &3, %8 means &7, so %n means &(n-1)*/
          array[i] = array[i>>1] + (i&1);
        }
        
        return array;
    }
}
