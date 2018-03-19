import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

class threeSum 
{
    public static List<List<Integer>> threeSum_now(int[] nums)
    {
        int i=0, j=0, other = 0, other_idx = 0, curr_target = 0, row_idx = 0, mask = 0;
        List<List<Integer>>  list = new ArrayList<List<Integer>>();
        List<Integer> no_dup = new ArrayList<Integer>();
        
        HashSet<Integer> set = new HashSet<Integer>();
        HashSet<Integer> seen = new HashSet<Integer>();
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(i=0; i<nums.length; i++)
        {
            if(seen.add(nums[i]))
            {
                no_dup.add(nums[i]);
            }
        }
        
        for(i=0; i<no_dup.size(); i++)
        {
            curr_target = (0 - no_dup.get(i));
            map.clear();
            
            for(j=0; j< no_dup.size(); j++)
            {
                if(j != i)
                {
                    if(map.containsKey(other = (curr_target - no_dup.get(j))))
                    {
                        other_idx = map.get(other);
                        
                        mask = ((1<<i) | (1<<other_idx) | (1<<j));
                        
                        if(set.add(mask))
                        {
                            list.add(new ArrayList<Integer>(3));
                            list.get(row_idx).add(no_dup.get(i));
                            list.get(row_idx).add(other);
                            list.get(row_idx).add(no_dup.get(j));
                            row_idx++;
                        }
                    }
                    
                    map.put(no_dup.get(j), j);
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
