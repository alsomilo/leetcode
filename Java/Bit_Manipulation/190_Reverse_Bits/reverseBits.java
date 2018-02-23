public class reverseBits 
{
    // you need treat n as an unsigned value
    public static int reverseBits_now(int n) 
	{
		n = (((n & 0xFFFF0000) >>> 16) | ((n & 0x0000FFFF) << 16));
		n = (((n & 0xFF00FF00) >>> 8)  | ((n & 0x00FF00FF) << 8));
		n = (((n & 0xF0F0F0F0) >>> 4)  | ((n & 0x0F0F0F0F) << 4));
		n = (((n & 0xCCCCCCCC) >>> 2)  | ((n & 0x33333333) << 2));
		n = (((n & 0xAAAAAAAA) >>> 1)  | ((n & 0x55555555) << 1));
		
		return n;
    }
	
	public static void main(String[] args)
	{
		System.out.println(reverseBits_now(2));
	}
}