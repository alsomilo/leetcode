/*
LC-187
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
*/

//Try not to use substring method

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