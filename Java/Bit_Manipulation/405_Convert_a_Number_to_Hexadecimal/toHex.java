import java.util.Stack;

class toHex 
{
    public static String toHex_new(int num) 
    {
    	String ret = "";
		int last_four_bits = 0;
		char   curr_char;
		Stack<String> stack = new Stack<String>();
		
		if(num == 0)
		{
			ret = "0";
		}
		else
		{
			
			while(num != 0)
			{
				last_four_bits = (num & 0xF);
				curr_char = (last_four_bits >= 10)? ((char)('a' + (last_four_bits-10))):((char)('0' + last_four_bits));
				stack.push(String.valueOf(curr_char));
				num >>>= 4;
			}
			
			while(!stack.empty())
			{
				ret += stack.pop();
			}
				
		}
		
		return ret; 
    }
    
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        System.out.println(n +" = 0x" + toHex_new(n));
    }
}
