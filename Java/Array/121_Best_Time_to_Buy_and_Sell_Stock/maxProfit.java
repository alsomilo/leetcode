class maxProfit 
{
	public static int maxProfit_now(int[] prices) 
    {
		int max = 0, i,j, delta =0;
		
		for(i=0; i<prices.length-1; i++)
		{
			for(j=i+1; j<prices.length;j++)
			{
				if(( delta = (prices[j] - prices[i])) > 0 && (delta > max))
				{
					max = delta;
				}
			}
		}
        return max;
    }
    
    public static void main(String[] args)
    {
        int i, size = args.length;
        int[] prices = new int[size];
        
        for(i=0; i<size; i++)
        {
            prices[i] = Integer.parseInt(args[i]);
        }
		
		System.out.println("Max profit is: " + maxProfit_now(prices));

    }
}
