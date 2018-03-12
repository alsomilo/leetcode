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
