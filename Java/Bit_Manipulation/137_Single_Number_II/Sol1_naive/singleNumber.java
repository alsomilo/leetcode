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


//082019: this solution used harsh set, to seperate unique number (shown at least once) and dup number (shown more than once), take the delta of (unique and dup), 
//the delta will be the number only shown once

import java.util.HashSet;

class singleNumber 
{
    public static int singleNumber_now(int[] nums)
    {
        int sum_set =0, sum_dup = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        HashSet<Integer> dup = new HashSet<Integer>();
        
        for(int i=0; i < nums.length; i++)
        {
            if(set.add(nums[i]) == false)
            {
                if(dup.add(nums[i]))
                {
                    sum_dup+=nums[i];
                }
            }
            else
            {
                sum_set+=nums[i];
            }
        }

        return (sum_set - sum_dup);
    }
    
    public static void main(String[] args)
    {       
        int size = args.length;
        int[] nums = new int[size];
        
        for(int i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
        
        System.out.println("single num is : " + singleNumber_now(nums));
    }
}
