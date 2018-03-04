import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class readBinaryWatch 
{    
    public static List<String> readBinaryWatch_new(int num) 
    {
        int h,m;
        List<String> ret_list = new ArrayList<String>();
        List<List<String>> hours_possible = new ArrayList<List<String>>();
        List<List<String>> mins_possible = new ArrayList<List<String>>();
        
        hours_possible.add(new ArrayList<String>(Arrays.asList("0")));
        hours_possible.add(new ArrayList<String>(Arrays.asList("1","2","4","8")));
        hours_possible.add(new ArrayList<String>(Arrays.asList("3","5","6","9","10")));
        hours_possible.add(new ArrayList<String>(Arrays.asList("7","11")));
        
        //0
        mins_possible.add(new ArrayList<String>(Arrays.asList("00")));
        
        //1
        mins_possible.add(new ArrayList<String>(Arrays.asList("01","02","04","08","16","32")));
        
        //2
        mins_possible.add(new ArrayList<String>(Arrays.asList("03","05","06","09","10","12","17","18","20","24","33","34","36","40","48")));
        
        //3
        mins_possible.add(new ArrayList<String>(Arrays.asList("07","11","13","14","19","21","22","25","26","28","35","37","38","41","42","44","49","50","52","56")));
        
        //4
        mins_possible.add(new ArrayList<String>(Arrays.asList("15","23","27","29","30","39","43","45","46","51","53","54","57","58")));
        
        //5
        mins_possible.add(new ArrayList<String>(Arrays.asList("31","47","55","59")));
        
        if(num < 0 || num > 8)
        {
            return ret_list;
        }
        
        for(h=0; h<=3 && h<=num; h++)
        {
            for(String hours: hours_possible.get(h))
            {
                m = num - h;
                
                if(m < 6)
                {
                    for(String mins: mins_possible.get(m))
                    {
                        ret_list.add(hours+":"+mins);
                    }
                }
                else
                {
                    break;
                }
            }        
        }
        
        return ret_list;
            
    }
    
    public static void main(String[] args)
    {
        int num = Integer.parseInt(args[0]);
        
        List<String> output = readBinaryWatch_new(num);
        
        for(String show : output)
        {
           System.out.println(show);
        }

    }
}
