import java.util.List;
import java.util.ArrayList;

class letterCasePermutation
{

    public static List<String> letterCasePermutation_new(String S)
    {
        List<String>  list = new ArrayList<String>();
        int i, j, len = S.length(), num_letter = 0, list_max = 0, curr_mask = 0;
        char c;
        String curr_string = "";
        
        for(i=0; i<len; i++)
        {
            c = S.charAt(i);
            
            if(Character.isLetter(c))
            {
                num_letter++;
            }
        }
        
        list_max = (1<<num_letter);
        
        for(i=0; i< list_max; i++)
        {
            if(i== 0)
            {
                list.add(S);
            }
            else
            {
                curr_string = "";
                curr_mask = i;
                
                for(j=len-1; j>=0; j--)
                {
                    c = S.charAt(j);
            
                    if(Character.isLetter(c))
                    {
                        
                        if((curr_mask & 1) != 0)
                        {
                            if(Character.isLowerCase(c))
                            {
                                curr_string = Character.toUpperCase(c) + curr_string;
                            }
                            else
                            {
                                curr_string = Character.toLowerCase(c) + curr_string;
                            }    

                        }
                        else
                        {
                            curr_string = String.valueOf(c) + curr_string;
                        }
                        
                        curr_mask >>= 1;
                    }
                    else
                    {
                        curr_string = String.valueOf(c) + curr_string;
                    }
                    
                }
                
                list.add(curr_string);
                
            }
        }
        
        return list;
    }
    
    public static void main(String[] args)
    {
        List<String>  list;
        
        list = letterCasePermutation_new(args[0]);

        for(String s : list)
        {
            System.out.println(s);
        }
    }
}