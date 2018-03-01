class getSum 
{
   
    public static int getSum_new(int a, int b)
    {
        int temp_sum =  a ^ b, carry = (a & b) <<1, overlap = 0;
        
        
        while((overlap = (temp_sum & carry)) != 0)
        {
            temp_sum ^= carry;
            carry = overlap << 1;
        }
        
        return (temp_sum ^ carry);
    }

    
    public static void main(String[] args)
	{
        int num1 = Integer.parseInt(args[0]), num2 = Integer.parseInt(args[1]);
		System.out.println(num1 + " + " + num2 + " = " + getSum_new(num1, num2));
	}
}
