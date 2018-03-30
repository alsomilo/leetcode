import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class findDuplicates 
{
	public static List<Integer> findDuplicates_now(int[] nums) 
    {
		List<Integer> list = new ArrayList<Integer>();
		List<Integer> input = new ArrayList<Integer>();
		int len = nums.length, i;
		
		for(i=0;i<len;i++)
		{
			input.add(nums[i]);
		}
		
		Collections.sort(input);
		
		for(i=1;i<len;i++)
		{
			if(input.get(i-1) == input.get(i))
			{
				list.add(input.get(i));
			}
		}
		
        return list;
    }
    
    public static void main(String[] args)
    {
        int i, size = args.length;
        int[] nums = new int[size];
		List<Integer> list;

        
        for(i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
		
		list = findDuplicates_now(nums);
		
		System.out.println("Duplicates are : ");
		
		for(Integer dup : list)
		{
			System.out.print( dup + " ");
		}
    }
}
