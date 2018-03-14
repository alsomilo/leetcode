class totalHammingDistance 
{
    public static int totalHammingDistance_new(int[] nums) 
    {
        int ret_val = 0, mask = 0, set_count = 0;
        
        for(int i=0; i<32; i++)
        {
            mask = (1 << i);
            set_count = 0;
            
            for(int val : nums)
            {                
                if((val & mask) != 0)
                {
                    set_count++;
                }
            }
            
            ret_val += set_count * (nums.length - set_count);
        }                
        
        return ret_val;
    }
    
    public static void main(String[] args)
    {       
        int size = args.length;
        int[] nums = new int[size];

        
        for(int i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
        
        System.out.println("Total hamming distance = " + totalHammingDistance_new(nums));

    }
}