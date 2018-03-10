class maxProduct 
{
    public static int maxProduct_new(String[] words) 
    {       
        int i,j,array_len = 0, max_prod = 0, curr_prod = 0;
        
        int[] lens, mask;
        
        if((words != null) && ((array_len = words.length) > 1))
        {
            lens = new int[array_len];
            mask = new int[array_len];
        
            for(i=0; i< array_len;i++)
            {
                lens[i] = words[i].length();
                mask[i] = 0;
            
                for(j=0; j< lens[i];j++)
                {
                    mask[i] |= 1 << (words[i].charAt(j) - 'a');
                }
            }
            
            for(i=0; i< array_len;i++)
            {
                for(j=i+1; j< array_len; j++)
                {
                    if((mask[i] & mask[j]) == 0)  // no repeated char
                    {
                        curr_prod = lens[i] * lens[j];
                        
                        if(curr_prod > max_prod)
                        {
                            max_prod = curr_prod;
                        }
                    }

                }            
            }
        
        }
        
        return max_prod;
    }
    
    public static void main(String[] args)
    {
        System.out.println("Max product is : " + maxProduct_new(args));
    }
}