import java.util.HashSet;

class findMaximumXOR 
{
    public static int findMaximumXOR_new(int[] nums) 
    {
        int i, j, max_xor_val = 0, temp_max_xor = 0, max_bit_idx = 0, curr_max_bit_idx = 0, mask = 0;
        
        for(i = 0; i < nums.length; i++)
        {
            if((curr_max_bit_idx = (31 - Integer.numberOfLeadingZeros(nums[i]))) > max_bit_idx)
            {
                max_bit_idx = curr_max_bit_idx;
            }      
        }
        
        
        for(i = max_bit_idx; i >= 0; i--)
        {
            mask |= (1 << i);
            HashSet<Integer> set = new HashSet<Integer>();
            
            for(j = 0; j < nums.length; j++)
            {
                set.add(nums[j] & mask);
            }
        
            temp_max_xor = (max_xor_val | (1 << i)); 
            
            for(Integer a : set)
            {
                if(set.contains( a ^ temp_max_xor))
                {
                    max_xor_val = temp_max_xor;
                    break;
                }
            }            
        }
        
        return max_xor_val;
        
    }
    
    public static void main(String[] args)
    {
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]), Integer.parseInt(args[3]), Integer.parseInt(args[4]), Integer.parseInt(args[5])};
        System.out.println("Max XOR value is : " + findMaximumXOR_new(nums));
    }
}