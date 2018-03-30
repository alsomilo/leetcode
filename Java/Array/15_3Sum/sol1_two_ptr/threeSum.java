import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class threeSum 
{
    public static List<List<Integer>> threeSum_now(int[] nums)
    {
        int i=0, j=0, len = nums.length, lo = 0, hi = 0, curr_target = 0, row_idx = 0;
        List<List<Integer>>  list = new ArrayList<List<Integer>>();
		List<Integer> input = new ArrayList<Integer>();

		for(i=0; i<nums.length; i++)
        {
            input.add(nums[i]);
        }  
		
		Collections.sort(input);
		
		for(Integer val : input)
		{
			System.out.print(val + " ");
		}
		
		for(i=0; i< len - 2; i++)
		{
			curr_target = (0 - input.get(i));
			
			if(i == 0 || (i>0 && (input.get(i) != input.get(i-1))))
			{
				lo = i+1;
				hi = len-1;
			
				while(lo < hi)
				{
					if(input.get(lo) + input.get(hi) == curr_target)
					{
						list.add(new ArrayList<Integer>(3));
						list.get(row_idx).add(input.get(i));
						list.get(row_idx).add(input.get(lo));
						list.get(row_idx).add(input.get(hi));
						row_idx++;
					
						while((lo < hi) && (input.get(lo++) == input.get(lo)))
						{
						}				
						while((lo < hi) && (input.get(hi--) == input.get(hi)))
						{
						}				
					}
					else if(input.get(lo) + input.get(hi) > curr_target)
					{
						hi--;
					}
					else
					{
						lo++;
					}
					
				}
			}
			
		}
        
        return list;
    }
    
    public static void printlist(List<List<Integer>> list) 
    {
        int row_idx = 0, col_idx = 0, total_row = list.size(), total_col = 0;
        
        System.out.println("There are " + total_row + " subsets, all subsets are:");
        System.out.println("{");
        
        for(row_idx = 0; row_idx<total_row; row_idx++)
        {
            System.out.print("  {");
            total_col = list.get(row_idx).size();
            
            for(col_idx = 0; col_idx<total_col; col_idx++)
            {
                System.out.print(list.get(row_idx).get(col_idx) +", "); 
            }
            
            System.out.println("} ");
        }
        
        System.out.println("}");
    }
    
    public static void main(String[] args)
    {
        int i, size = args.length;
        int[] nums = new int[size];
        List<List<Integer>>  list;
        
        for(i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
        
        list = threeSum_now(nums);
        printlist(list);

    }
}
