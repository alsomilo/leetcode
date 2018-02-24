class missingNumber 
{
    public static int missingNumber_new(int[] nums) 
    {
        //given there is one missing num in the array
        int count_t = (nums.length + 1);
        
        int sum_t = ((count_t - 1) * count_t) >> 1, sum_arr = 0;
        
        for(int i = 0; i < nums.length; i++)
        {
            sum_arr += nums[i];
        }
        
        return (sum_t - sum_arr);
        
        
    }
    
    public static void main(String[] args)
    {
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]), Integer.parseInt(args[3]), Integer.parseInt(args[4])};
        System.out.println("missing numer is : " + missingNumber_new(nums));
    }
}