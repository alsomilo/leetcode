public class hasAlternatingBits 
{
    public static boolean hasAlternatingBits_now(int n) 
	{
        return ((n >>> 1) == (~n & (( Integer.highestOneBit(n)<< 1) - 1)));
    }
	
	public static void main(String[] args)
	{
        int num = Integer.parseInt(args[0]);
		System.out.println( num + " has alternating bits? " + hasAlternatingBits_now(num));
	}
}