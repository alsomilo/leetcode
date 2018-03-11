import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;

class maxProduct 
{
    public static int maxProduct_new(String[] words) 
    {       
        int i,j,array_len = 0, max_prod = 0, curr_prod = 0, max_i=0, max_j=0;
        
        class Combo implements Comparable<Combo> 
        {
            int org_index;
            int mask;
            int len;
            
            @Override
            public int compareTo(Combo other)
            {
                //Ascending
                //return  (this.len - other.len);
                
                //Descending
                return  (other.len - this.len);
            }
            
            @Override
            public String toString()
            {
                return  (org_index + ": mask= " + mask + " len= " + len);
            }
        }
        
        if((words != null) && ((array_len = words.length) > 1))
        {
            ArrayList<Combo> list = new ArrayList<Combo>(array_len);
        
            for(i=0; i< array_len;i++)
            {
                Combo element = new Combo();
                
                element.org_index = i;
                element.mask = 0;
                element.len  = words[i].length();               
            
                for(j=0; j< element.len ; j++)
                {
                    element.mask|= 1 << (words[i].charAt(j) - 'a');
                }
                
                list.add(element);
                
            }
            
            Collections.sort(list);
            

            for(Combo print : list)
            {
                System.out.println(print);
            }

            
            
            for(i=0; i<array_len; i++)
            {
                for(j=i+1; j<array_len; j++)
                {
                    if((list.get(i).mask & list.get(j).mask) == 0)
                    {
                        curr_prod = list.get(i).len * list.get(j).len;
                        
                        if(curr_prod > max_prod)
                        {
                            max_prod = curr_prod;
                            max_i = list.get(i).org_index;
                            max_j = list.get(j).org_index;
                        }
                        
                    }
                }
                
            }
        
        }
        
        System.out.println("words[" + max_i +"]= " +  words[max_i]); 
        System.out.println("words[" + max_j +"]= " +  words[max_j]); 
        System.out.println("have the max product");
        
        return max_prod;
    }
    
    public static void main(String[] args)
    {
        System.out.println("Max product is : " + maxProduct_new(args));
        //maxProduct_new(args);
    }
}