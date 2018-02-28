import java.util.LinkedList;

public class singleNumber 
{
    public static int[] singleNumber_new(int[] nums) 
    {
        int[] array;
        int list_size, i;
        
        LinkedList<Integer> list = new LinkedList<Integer>();
        
        for(i = 0; i < nums.length; i++)
        {
            if(list.contains(nums[i]))
            {
                list.remove((Integer)nums[i]);
            }
            else
            {
                list.add(nums[i]);
            }
        }
        
        list_size = list.size();
        array = new int[list_size];
        
        for(i=0; i<list_size; i++ )
        {
            array[i] = list.get(i);
        }
        
        return array;
    }
    
    public static void main(String[] args)
    {
        int[] nums = {Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]), Integer.parseInt(args[3]), Integer.parseInt(args[4]), Integer.parseInt(args[5])};
        int[] output;
        int   output_size; 
        
        output = singleNumber_new(nums);
        output_size = output.length;
        
        System.out.println("There are " + output_size + " numbers only show up once: ");
        for(int i=0; i<output_size; i++)
        {
            System.out.print(output[i] + ", ");
        }
            
    }
}
