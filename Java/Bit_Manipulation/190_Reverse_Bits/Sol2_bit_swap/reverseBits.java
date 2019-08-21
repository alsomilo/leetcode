public class reverseBits 
{
    // you need treat n as an unsigned value
    public static int reverseBits_now(int n) 
	{
		int min = 1, max = (1 << 31), ret = 0;
		 
		for(int i = 0; i < 16; i++)
		{
			ret |= ((n & (min << i)) << (31 - (i << 1)) |
					(n & (max >>> i)) >>> (31 - (i << 1)));
		}
		
		return ret;
    }
	
	public static void main(String[] args)
	{
		System.out.println(reverseBits_now(Integer.parseInt(args[0])));
	}
}