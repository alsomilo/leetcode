import java.util.HashMap;

class twoSum 
{
    public static int[] twoSum_now(int[] nums, int target)
    {
        int i=0, other = 0;
        int[] results = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(i=0; i<nums.length; i++)
        {
            if(map.containsKey(other = (target - nums[i])))
            {
                results[0] = map.get(other);
                results[1] = i;
                break;
            }
            
            map.put(nums[i], i);
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
