class getSum 
{
   
    public static int getSum_new(int a, int b)
    {
        int temp_sum =  a ^ b, advance = (a & b) <<1, temp_val = 0;
        
        
        while((temp_sum & advance) != 0)
        {
            temp_val = temp_sum;
            temp_sum ^= advance;
            advance = (temp_val & advance) << 1;
        }
        
        return (temp_sum ^ advance);
    }

    
    public static void main(String[] args)
	{
        int num1 = Integer.parseInt(args[0]), num2 = Integer.parseInt(args[1]);
		System.out.println(num1 + " + " + num2 + " = " + getSum_new(num1, num2));
	}
}
