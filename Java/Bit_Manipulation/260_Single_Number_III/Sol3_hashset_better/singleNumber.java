import java.util.HashSet;

class singleNumber 
{
    public static int[] singleNumber_now(int[] nums) 
    {
        int[] array = new int[2];
		int i = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        
        for(i=0; i < nums.length; i++)
        {
            if(set.contains(nums[i]))
            {
                set.remove(nums[i]);
            }
			else
			{
				set.add(nums[i]);
			}
        }

        i = 0;
		
        for(Integer each : set)
        {
            array[i++] = each;
        }

        return array;
    }
    
    public static void main(String[] args)
    {       
        int size = args.length, output_size;
        int[] nums = new int[size], output;

        
        for(int i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
        
        output = singleNumber_now(nums);
        output_size = output.length;
        
        System.out.println("There are " + output_size + " numbers only show up once: ");
        
        for(int i=0; i<output_size; i++)
        {
            System.out.println(output[i]);
        }
    }
}
