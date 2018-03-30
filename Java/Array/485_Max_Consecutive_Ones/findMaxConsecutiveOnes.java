class findMaxConsecutiveOnes 
{
	public static int findMaxConsecutiveOnes_now(int[] nums)
    {
        int max_cnt = 0, curr_cnt = 0;
		for(int i=0; i< nums.length;i++)
		{
			if(nums[i] == 1)
			{
				curr_cnt++;
			}
			else
			{
				if(curr_cnt > max_cnt)
				{
					max_cnt = curr_cnt;
				}
				curr_cnt = 0;
			}
		}
        
		if(curr_cnt > max_cnt)
		{
			max_cnt = curr_cnt;
		}
		
        return max_cnt;
    }
    
    public static void main(String[] args)
    {
        int i, size = args.length;
        int[] nums = new int[size];

        
        for(i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }

        System.out.println("Max consecutive ones = " + findMaxConsecutiveOnes_now(nums));
    }
}
