public class findTheDifference 
{
    public static char findTheDifference_new(String s, String t) 
    {
        int i,xor = 0;
        
        for(i=0; i<s.length(); i++)
        {
            xor ^= ((int)s.charAt(i));
        }
        
        for(i=0; i<t.length(); i++)
        {
            xor ^= ((int)t.charAt(i));
        }
        
        return (char)xor;
    }
    
    public static void main(String[] args)
    {
        System.out.println("Missing char is: " + findTheDifference_new(args[0], args[1]));           
    }
}

