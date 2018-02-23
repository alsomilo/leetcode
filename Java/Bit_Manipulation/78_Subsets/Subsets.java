import java.util.List;
import java.util.ArrayList;

class Subsets 
{
    public static boolean is_bit_present(int mask_in, int bit_idx_in)
    {
      return ((mask_in & (1 << bit_idx_in)) != 0);
    }
    
    public static List<List<Integer>> subsets(int[] nums) 
    {
        int row_idx = 0, bit_idx = 0, mask = 0, total_row = (int)Math.pow(2, nums.length);
        List<List<Integer>> ret_list = new ArrayList<List<Integer>>(total_row);
        
        for(row_idx = 0; row_idx<total_row; row_idx++)
        {
            ret_list.add(new ArrayList<Integer>());
            
            mask = row_idx;
            for(bit_idx = 0; bit_idx<nums.length; bit_idx++)
            {
                if(is_bit_present(mask, bit_idx))
                {
                    ret_list.get(row_idx).add(nums[bit_idx]);
                }
            }
            //System.out.println("row_idx = "+ row_idx + " has ArrayList created !");
        }
        //System.out.println("total row = "+total_row + " !");     
        
        return ret_list;
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
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]), Integer.parseInt(args[3]), Integer.parseInt(args[4])};
        List<List<Integer>>  list;
        
        list = subsets(nums);
        printlist(list);
    }
}