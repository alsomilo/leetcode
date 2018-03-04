import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;

class findRepeatedDnaSequences 
{
    
    public static List<String> findRepeatedDnaSequences_new(String s) 
    {
        List<String> ret_list = new ArrayList<String>();
        HashSet<String> seen = new HashSet<String>();
        HashSet<String> repeat = new HashSet<String>();
        
        for(int i=0; (i+9) < s.length(); i++)
        {
            String curr_sub_string = s.substring(i,i+10);
                
            if( false == seen.add(curr_sub_string) )
            {
                if(repeat.add(curr_sub_string))
                {
                    ret_list.add(curr_sub_string);
                }
            }
        }         
        
        return ret_list;
    }

    
    public static void main(String[] args)
    {
        
        List<String> output = findRepeatedDnaSequences_new(args[0]);
        
        for(String show : output)
        {
           System.out.println(show);
        }
    }
}