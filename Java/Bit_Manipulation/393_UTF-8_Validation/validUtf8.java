class validUtf8 
{
    public static boolean validUtf8_now(int[] data)
    {
        int num = 0, proc_idx = 0, proc_len = 0, data_len = data.length;
        boolean is_utf8 = true;
        
        do
        {
            num = (data[proc_idx] & 0xFF);
            
            if((num & 0x80) == 0)
            {
                proc_idx++;
            }
            else
            {
                proc_len = Integer.numberOfLeadingZeros(num ^ 0xFF) - 24;
                
                if((proc_len == 1)||
                    (proc_len > 4))
                {
                    is_utf8 = false;
                    break;
                }
                
                if(proc_idx + proc_len-1 >= data_len)
                {
                    is_utf8 = false;
                    break;                  
                }
                
                for(int i=1; i< proc_len; i++)
                {
                    if((data[proc_idx+i] & 0xC0) != 0x80)
                    {
                        is_utf8 = false;
                        break;
                    }
                }
                
                if(!is_utf8)
                {
                    break;
                }
                
                proc_idx += proc_len;
            }
            
        }while(proc_idx < data_len);
        
        
        return is_utf8;

    }
    
    public static void main(String[] args)
    {       
        int size = args.length;
        int[] nums = new int[size];

        
        for(int i=0; i<size; i++)
        {
            nums[i] = Integer.parseInt(args[i]);
        }
        
        System.out.println("Is UTF-8? " + validUtf8_now(nums));

    }
}
