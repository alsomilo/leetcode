class isToeplitzMatrix 
{

	public static boolean isToeplitzMatrix_now(int[][] matrix) 
    {
		boolean ret_val = true;
		int i,j;
		
		for(i=0;i<matrix.length-1;i++)
		{
			for(j=0;j<matrix[i].length-1;j++)
			{
				if(matrix[i][j] != matrix[i+1][j+1])
				{
					ret_val = false;
					break;
				}
			}
		}
		
        return ret_val;
    }
    
    public static void main(String[] args)
    {
		int[][] matrix = 
		{
			{1,2,3,4},
			{5,1,2,3},
			{9,5,1,2}
		};
			
		System.out.println("is ToeplitzMatrix ? " + isToeplitzMatrix_now(matrix));

    }
}
