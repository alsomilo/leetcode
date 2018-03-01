public class findTheDifference 
{
    public static char findTheDifference_new(String s, String t) 
    {
        int i, xor = 0;
        
        s+=t;
        
        for(i=0; i<s.length(); i++)
        {
            xor ^= ((int)s.charAt(i));
        }
        
        return (char)xor;
    }
    
    public static void main(String[] args)
    {
        System.out.println("Missing char is: " + findTheDifference_new(args[0], args[1])); 
        System.out.println("String s is: " + args[0]); 
        System.out.println("String t is: " + args[1]); 
    }
}

