class matrixReshape 
{
	public static int[][] matrixReshape_now(int[][] nums, int r, int c) 	
    {
		int[][] output;
		int i,j,r_in=0, c_in=0, r_in_num=0, c_in_num=0, total=0, counter=0;
		
		r_in_num = nums.length;
		c_in_num = nums[0].length;
		output = new int[r][c];
		
		if((total = (r_in_num * c_in_num)) != r*c)
		{
			System.out.println("error: input is invalid, can not reshape");
		}
		else
		{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					r_in = counter / c_in_num;
					c_in = counter % c_in_num;
					output[i][j] = nums[r_in][c_in];
					
					counter++;
				}
			}
		}
        return output;
    }
    
    public static void main(String[] args)
    {
		int[][] nums = 
		{
			{1,2,3,4},
			{5,1,2,3},
			{9,5,1,2}
		};
		int[][] out;
		            
		int r = Integer.parseInt(args[0]);
		int c = Integer.parseInt(args[1]);
		
		out = new int[r][c];
		
		System.out.println("After reshape : (" + r + " x " + c + ")");
		
		out = matrixReshape_now(nums, r, c);
		
		for(int i=0 ; i<r; i++)
		{
			System.out.print("{");
						
			for(int j=0; j<c; j++)
			{
				System.out.print(out[i][j] + ", ");
			}
			
			System.out.println("}");
		}

    }
}
