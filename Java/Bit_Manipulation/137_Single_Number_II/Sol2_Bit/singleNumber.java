class singleNumber {
    public static int singleNumber_now(int[] nums) 
	{	
		int mask = 0, count = 0, ret = 0;
		
		for(int i = 0; i < 32; i++)
		{
			mask = (1 << i);
			count = 0;
			
			for(int j = 0; j < nums.length; j++)
			{
				if((nums[j] & mask) != 0)
				{
					count++;
				}
				
			}
			
			if((count % 3) != 0)
			{
				ret |= mask;
			}
			
		}
		
		return ret;
        
    }
	
	public static void main(String[] args){
		int size = args.length;
		
		int[] array = new int[size];
		
		for(int i=0; i<size; i++)
		{
			array[i] = Integer.parseInt(args[i]);
		}
		
		System.out.println("Single number is " + singleNumber_now(array));
		
	}
	
}