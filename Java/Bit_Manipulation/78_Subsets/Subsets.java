import java.util.List;
import java.util.ArrayList;

class Subsets 
{
    public static List<List<Integer>> subsets(int[] nums) 
    {
        int idx = 0, total_row = (int)Math.pow(2, nums.length);
        List<List<Integer>> ret_list = new ArrayList<List<Integer>>(total_row);
        
        for(idx = 0; idx<total_row; idx++)
        {
            ret_list.add(new ArrayList<Integer>());
            System.out.println("row idx = "+ idx + " has ArrayList created !");
        }
        
        System.out.println("total row = "+total_row + " !");
        return ret_list;
    }
    
    public static void main(String[] args)
    {
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2])};
        subsets(nums);
    }
}