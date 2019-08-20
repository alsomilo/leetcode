/*
LC-137

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
*/


//082019: this is a genric solution applies to any accurance of dup numbers. The trick here is to use sum_bit_i % N to cancel the duplicated numbers, N is the repeated times for dup numbers.
//  sum_bit_i % N  == 1 means that unique value has bit i set.



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