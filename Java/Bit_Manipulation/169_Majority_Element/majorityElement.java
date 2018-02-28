import java.util.HashMap;

public class majorityElement
{
	public static int majorityElement_new(int[] nums)
	{

    	HashMap<Integer, Integer> stats = new HashMap<Integer, Integer>();
    	int max=0, maxkey=0;

	    for(int i=0; i<nums.length; i++)
    	{

        	if(stats.containsKey(nums[i]))
        	{
            	stats.put(nums[i], stats.get(nums[i])+1);
        	}	
	        else
    	    {
        	    stats.put(nums[i], 0);
        	}  
     	}    

    	for (HashMap.Entry<Integer, Integer> entry : stats.entrySet())
		{
    		if(entry.getValue() >= max)
    		{	
	    	    max=entry.getValue();
	    	    maxkey=entry.getKey();
	    	}  
		} 

    	return maxkey;
	}

	public static void main(String[] args)     	
	{
		int[] nums = {1};
		System.out.println("majority element is: "+majorityElement_new(nums));
	}

}
