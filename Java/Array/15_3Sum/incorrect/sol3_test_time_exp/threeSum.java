import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class threeSum 
{
    public static List<List<Integer>> threeSum_now(int[] nums)
    {
        int i=0, j=0, other = 0, curr_target = 0, row_idx = 0, neg_cnt =0, zero_cnt = 0, prev_target = 0, prev_element = 0;
        List<List<Integer>>  list = new ArrayList<List<Integer>>();
        
        List<Integer> input = new ArrayList<Integer>();
        List<Integer> map = new ArrayList<Integer>();
        
        if(nums.length < 3)
        {
            return list;
        }
        
        for(i=0; i<nums.length; i++)
        {
            if(nums[i] < 0) 
            {
                neg_cnt++;
            }
            else if(nums[i] == 0)
            {
                zero_cnt++;
            }
            
            input.add(nums[i]);
        }   
        
        Collections.sort(input);
        
        if(neg_cnt == 0)
        {
            if(input.get(0) + input.get(1) + input.get(2) == 0)
            {
                list.add(new ArrayList<Integer>(3));
                list.get(row_idx).add(0);
                list.get(row_idx).add(0);
                list.get(row_idx).add(0);
            }

            return list;
        }
        
        for(i=neg_cnt; i< nums.length; i++)
        {
            curr_target = 0 - input.get(i);
            
            if(curr_target != prev_target)
            {
                map.clear();
            
                for(j=0; j< neg_cnt; j++)
                {
                       
                    if(map.contains(other = (curr_target - input.get(j))))
                    {
                        if((input.get(j) != prev_element) ||
                            ((input.get(j) == prev_element) && (prev_element == other)))
                        {
                            list.add(new ArrayList<Integer>(3));

                            list.get(row_idx).add(other);
                            list.get(row_idx).add(input.get(j));
                            list.get(row_idx).add(input.get(i));
                    
                            row_idx++;
                            
                            if( (row_idx > 1) &&
                                (list.get(row_idx-1).get(0) == list.get(row_idx-2).get(0)) &&
                                (list.get(row_idx-1).get(1) == list.get(row_idx-2).get(1)) &&
                                (list.get(row_idx-1).get(2) == list.get(row_idx-2).get(2)))
                            
                            {
                                row_idx--;
                                list.remove(row_idx);
                            }
                        }
                        
                    }
                    
                    map.add(input.get(j));
                    prev_element = input.get(j);
                    

                }
            }
            
            prev_target = curr_target;
            
        }
        
        for(i=0; i< neg_cnt; i++)
        {
            curr_target = 0 - input.get(i);
            
            if(curr_target != prev_target)
            {
                map.clear();
            
                for(j=neg_cnt; j< nums.length; j++)
                {

                    if(map.contains(other = (curr_target - input.get(j))))
                    {
                        if((input.get(j) != prev_element) ||
                                ((input.get(j) == prev_element) && (prev_element == other)))
                        {
                            list.add(new ArrayList<Integer>(3));
                            list.get(row_idx).add(input.get(i));
                            list.get(row_idx).add(other);
                            list.get(row_idx).add(input.get(j));
                    
                            row_idx++;
                            
                            if( (row_idx > 1) &&
                                (list.get(row_idx-1).get(0) == list.get(row_idx-2).get(0)) &&
                                (list.get(row_idx-1).get(1) == list.get(row_idx-2).get(1)) &&
                                (list.get(row_idx-1).get(2) == list.get(row_idx-2).get(2)))
                            
                            {
                                row_idx--;
                                list.remove(row_idx);
                            }
                        }
                    }
                    
                    map.add(input.get(j));
                    prev_element = input.get(j);
                    

                }
            }
            
            prev_target = curr_target;
            
        }
        
        if(zero_cnt >= 3)
        {
            list.add(new ArrayList<Integer>(3));
            list.get(row_idx).add(0);
            list.get(row_idx).add(0);
            list.get(row_idx).add(0);
            
            row_idx++;
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
