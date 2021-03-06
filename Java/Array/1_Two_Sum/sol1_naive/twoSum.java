import java.util.ArrayList;

class twoSum 
{
    public static int[] twoSum_now(int[] nums, int target)
    {
        int i=0, other = 0, other_idx = 0;
        int[] results = new int[2];
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for(i=0; i<nums.length; i++)
        {
            list.add(nums[i]);
        }
        
        for(i=0; i<nums.length; i++)
        {
            if(list.contains(other = (target - nums[i])))
            {
                if(i != (other_idx  = list.indexOf(other)))
                {
                    results[0] = i;
                    results[1] = other_idx;
                    break;
                }
            }
        }
        
        return results;
    }
    
    public static void main(String[] args)
    {
        int i, size = args.length, target = 0;
        int[] nums = new int[size-1], results = new int[2];

        
        for(i=0; i<(size-1); i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
        
        target = Integer.parseInt(args[i]);
        
        results = twoSum_now(nums, target);

        System.out.println("indexes are : " + results[0] + " and " + results[1]);
    }
}
