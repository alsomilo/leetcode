class singleNumber 
{
    public static int singleNumber_now(int[] nums)
    {
        int ret_val = 0;
        
        for(int i=0; i < nums.length; i++)
        {
            ret_val ^= nums[i];
        }
        
        return ret_val;
    }
    
    public static void main(String[] args)
    {
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]), Integer.parseInt(args[3]), Integer.parseInt(args[4])};
        System.out.println("single num is : " + singleNumber_now(nums));
    }
}
