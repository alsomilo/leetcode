class isPowerOfFour 
{
    public static boolean isPowerOfFour_new(int num) 
    {
        return  ( (num > 0) &&            
                  ((num & (num-1)) == 0) &&
                   ((num & 0x55555555) !=0 ) );
        
    }
    
    public static void main(String[] args)
    {
        int num = Integer.parseInt(args[0]);
        System.out.println(num + " is a power of 4? " + isPowerOfFour_new(num));
    }
}
