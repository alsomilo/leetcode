/*
LC-136

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
*/

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
