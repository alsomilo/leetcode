public class findComplement 
{
    // you need treat n as an unsigned value
    public static int findComplement_now(int num) 
	{
		return (~num & ((Integer.highestOneBit(num) << 1)-1));
    }
	
	public static void main(String[] args)
	{
		System.out.println(findComplement_now(Integer.parseInt(args[0])));
	}
}