class integerReplacement 
{
    public static int integerReplacement_new(int n) 
    {
		int num = n, counter = 0;
		
		if(num > 0)
		{
			while(num != 1)
			{
				if((num & 1) == 0)
				{
					num >>>= 1;
				}
				else
				{
					if((num != 3) && ((num & 3) == 3))
					{
						num++;
					}
					else
					{
						num--;
					}
				}
			
				counter++;
			}
		}
		else
		{
			System.out.println("n <= 0! must be positive!!");
		}
		
		return counter;
    }
    
    public static void main(String[] args)
    {       
        System.out.println("Needs " + integerReplacement_new(Integer.parseInt(args[0])) + " rounds to reach 1");
    }
}