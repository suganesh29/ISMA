
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.text.DecimalFormat;

class Main
{
  public static int size;

  static ArrayList < Integer > colMaxSum (double matrix[][])
  {
    // Variable to store index of row 
    // with maximum 
    int idx = -1;

    // Variable to store maximum sum 
    int maxSum = Integer.MIN_VALUE;
    //System.out.println("Hello");
    // Traverse the matrix row wise 
    for (int i = 0; i < size; i++)
      {
	int sum = 0;
	for (int j = 0; j < size; j++)
	  {
	    sum += matrix[i][j];
	  }

	// Update maxSum if it is less than 
	// current row sum 
	if (maxSum < sum)
	  {
	    maxSum = sum;

	    // store index 
	    idx = i;
	  }
      }

    // Arraylist to store values of index 
    // of maximum sum and the maximum sum together 
    ArrayList < Integer > res = new ArrayList <> ();
    res.add (idx);
    res.add (maxSum);

    return res;
  }

  public static void printMatrix (int size, double[][]m)
  {
    System.out.println ("---------------------------------------");
    for (int i = 0; i < size; i++)
      {
	for (int j = 0; j < size; j++)
	  {
	    	System.out.print ("\t ");
	    	System.out.printf ("%.2f ", m[i][j]);
	  }
	System.out.println ();
      }
  }

  public static void removeNegZero (int size, double[][]m)
  {
    for (int i = 0; i < size; i++)
      {
	for (int j = 0; j < size; j++)
	  {
	    if (m[i][j] == -0.0)
	      {
		m[i][j] = 0;
	      }
	  }
      }
  }

  public static void makeReducedEchelon (double[][]mmatrix,
					 double[][]identity, int size, int i)
  {
    int count = 1;
    double matrixMultiple1 = mmatrix[i][i];

    for (int j = i; j > 0; j--)
      {
	if (mmatrix[i - count][i] != 0)
	  {
	    double temp = 0;
	    double matrixMultiple2 = mmatrix[i - count][i];

	    for (int k = 0; k < size; k++)
	      {
		temp =
		  (mmatrix[i - count][k] * matrixMultiple1) -
		  (mmatrix[i][k] * matrixMultiple2);
		mmatrix[i - count][k] = temp;

		temp =
		  (identity[i - count][k] * matrixMultiple1) -
		  (identity[i][k] * matrixMultiple2);
		identity[i - count][k] = temp;
	      }
	  }
	count++;
      }
  }

  public static void makeEchelon (double[][]mmatrix, double[][]identity,
				  int size, int i)
  {
    int count = 1;
    double matrixMultiple1 = mmatrix[i][i];

    for (int j = i; j < size - 1; j++)
      {
	if (mmatrix[i + count][i] != 0)
	  {
	    double temp = 0;
	    double matrixMultiple2 = mmatrix[i + count][i];

	    for (int k = 0; k < size; k++)
	      {
		temp =
		  (mmatrix[i + count][k] * matrixMultiple1) -
		  (mmatrix[i][k] * matrixMultiple2);
		mmatrix[i + count][k] = temp;

		temp =
		  (identity[i + count][k] * matrixMultiple1) -
		  (identity[i][k] * matrixMultiple2);
		identity[i + count][k] = temp;
	      }
	  }
	count++;
      }
  }

  public static void checkPivot (double[][]mmatrix, double[][]identity,
				 int size, int oldRow)
  {
    if (mmatrix[oldRow][oldRow] == 0)
      {

	//Scanning other rows with non-zero entries in that row and column. Starting from bottom
	int newRow = 0;
	for (int j = size - 1; j > oldRow; j--)
	  {
	    if (mmatrix[j][oldRow] != 0)
	      {
		newRow = j;
		break;
	      }
	  }

	//Now Replace the Row "i" with Row "newRow"
	double temp;
	for (int j = 0; j < size; j++)
	  {
	    temp = mmatrix[oldRow][j];
	    mmatrix[oldRow][j] = mmatrix[newRow][j];
	    mmatrix[newRow][j] = temp;

	    temp = identity[oldRow][j];
	    identity[oldRow][j] = identity[newRow][j];
	    identity[newRow][j] = temp;
	  }
      }

  }				// Driver code 
  public static void main (String[]args)
  {


    //int i,j,k;

    Scanner in = new Scanner (System.in);
    System.out.print ("Enter the size of the nxn Matrix: ");
    size = in.nextInt ();


    System.out.println ("The order of the matrix" + size);


    double[][] matrix = new double[size][size];
    double[][] NormalizingMat = new double[1000][1000];	// Normalizing Mattix
    DecimalFormat df = new DecimalFormat();
      df.setMaximumFractionDigits(3);

    System.out.println ("Enter matrix elements");
    for (int i = 0; i < size; i++)
      {
	System.out.print ("Enter the Values for Row " + (i + 1) + ": ");
	for (int j = 0; j < size; j++)
	  {
	    matrix[i][j] = in.nextDouble ();
	  }

      }



    System.out.println ("The matrix is");
    System.out.println ("---------------------------------------");
    for (int i = 0; i < size; i++)
      {
	for (int j = 0; j < size; j++)
	  {
	    System.out.print ("\t ");
	    System.out.print (matrix[i][j] + "\t");
	  }
	System.out.println ();

      }


    ArrayList < Integer > ans = colMaxSum (matrix);
    System.out.println ("---------------------------------------");
    System.out.println ("Row " + (ans.get (0) + 1) + " has max sum " +
			ans.get (1));

    int maxp = ans.get (1);
    double[][] Xmatrix;		//X matrix
    Xmatrix = new double[size][size];
    double[][] identity;	//I matrix
    identity = new double[size][size];
    double[][] mmatrix;		//I -X  matrix
    mmatrix = new double[size][size];
    double[][] Tmatrix;		//T  matrix
    Tmatrix = new double[size][size];
    int row, col;



       double[] sumRow;		// Ri 
       sumRow = new double[size];
       double[] sumCol;		// Ci 
       sumCol = new double[size];
       
      double[] RiplusCi;		// Ri+Ci 
      RiplusCi = new double[size]; 
       
       double[] RiminusCi;		// Ri+Ci 
      RiminusCi = new double[size]; 
      
       
       double rows, cols;  
       rows = Tmatrix.length;  
       cols = Tmatrix[0].length;  
    
    System.out.println ();
    System.out.println ();
    System.out.println ();
    System.out.println ("D  matrix  values:");
    System.out.println ("---------------------------------------");
    for (row = 0; row < size; row++)
      {
	for (col = 0; col < size; col++)
	  {
	    NormalizingMat[row][col] = matrix[row][col];
	    Xmatrix[row][col] = NormalizingMat[row][col] / maxp;
	    System.out.print ("\t ");
	    System.out.print(df.format(Xmatrix[row][col]));
	    //System.out.print (Xmatrix[row][col] + "\t");

	  }
	System.out.println ();
      }


    
    System.out.println ();
    System.out.println ();
    System.out.println ();
    System.out.println ("I matrix  values:");
    System.out.println ("---------------------------------------");
    for (row = 0; row < size; row++)
      {
	for (col = 0; col < size; col++)
	  {
	    if (row == col)
	      {
		identity[row][col] = 1;
	      }
	    else
	      {
		identity[row][col] = 0;
	      }

	    System.out.print ("\t ");
	    
	    System.out.printf ("%.2f ", identity[row][col]);
	   
	  }
	System.out.println ();
      }




    System.out.println ();
    System.out.println ();
    System.out.println (("(I- D) values:"));
    System.out.println ("---------------------------------------");
    for (row = 0; row < size; row++)
      {
	for (col = 0; col < size; col++)
	  {

	    mmatrix[row][col] = identity[row][col] - Xmatrix[row][col];

	    System.out.print ("\t ");
	    System.out.printf ("%.2f ", mmatrix[row][col]);
	    
	  }
	System.out.println ();
      }

    int temp = 0;
        for (int i = 0; i < size - 1; i++)
          {
    	//Check If Pivot is Zero Interchange it with some other row
    	checkPivot (mmatrix, identity, size, i);
    
    	if ((mmatrix[i][i] != 1) & (mmatrix[i][i] != 0))
    	  {
    	    //Making the pivot 1 of every row.
    	    double matrixValue = mmatrix[i][i];
    
    	    for (int j = 0; j < size; j++)
    	      {
    		mmatrix[i][j] = mmatrix[i][j] / matrixValue;
    		identity[i][j] = identity[i][j] / matrixValue;
    	      }
    	  }
    	makeEchelon (mmatrix, identity, size, i);
          }
        //Making the Pivot of Last Row 1.
        if ((mmatrix[size - 1][size - 1] != 1) & (mmatrix[size - 1][size - 1] !=
    					      0))
          {
    	//Making the pivot 1 of every row.
    	double matrixValue = mmatrix[size - 1][size - 1];
    	for (int j = 0; j < size; j++)
    	  {
    	    mmatrix[size - 1][j] = mmatrix[size - 1][j] / matrixValue;
    	    identity[size - 1][j] = identity[size - 1][j] / matrixValue;
    	  }
          }
        removeNegZero (size, mmatrix);
        removeNegZero (size, identity);
    
        int singularCount = 0;
        for (int i = 0; i < size; i++)
          {
    	singularCount = 0;
    	for (int j = 0; j < size; j++)
    	  {
    	    if (mmatrix[i][j] == 0)
    	      {
    		singularCount++;
    	      }
    	  }
          }
    
        if (singularCount == size)
          {
    	System.out.
    	  println
    	  ("\nThe matrix is Singular. So, It'sInverse doesn't exist.");
          }
        else
          {
    	for (int i = size - 1; i > 0; i--)
    	  {
    	    makeReducedEchelon (mmatrix, identity, size, i);
    	  }
    	System.out.println ("\n (D-I)^1");
    	printMatrix (size, identity);

	System.out.println ();
	System.out.println ();
	System.out.println ();
	System.out.println ("T= D(D-I)-1   matrix  values:");
	System.out.println ("---------------------------------------");



	for (row = 0; row < size; row++)
	  {
	    for (col = 0; col < size; col++)
	      {
		Tmatrix[row][col] = 0;
		for (int kk = 0; kk < size; kk++)
		  {
		    Tmatrix[row][col] += Xmatrix[row][kk] * identity[kk][col];


		  }

		System.out.print ("\t ");
		System.out.printf ("%.2f ", Tmatrix[row][col]);
	      }
	    System.out.println ();
	  }

      }

    System.out.println ();
    System.out.println ();
    System.out.println ();

   
       //DecimalFormat df = new DecimalFormat();
       df.setMaximumFractionDigits(3);
      //System.out.println ("Ri   values:");
	  //System.out.println ("---------------------------------------");
//Calculates sum of each row of given matrix  
        for(int i = 0; i < rows; i++){  
            //sumRow =0;  
            for(int j = 0; j < cols; j++){  
              sumRow[i] = sumRow[i]+ Tmatrix[i][j];  
            }  
      }
       for(int i = 0; i < cols; i++){  
             
            for(int j = 0; j < rows; j++){  
              sumCol[i] = sumCol[i]+ Tmatrix[j][i];  
            }  
       }
            
            
// Print Ri and Ci  values

        System.out.println ("      Ri Values         Ci Values:");
	    System.out.println ("---------------------------------------");
        for(row= 0; row < size; row++)
                { 
                 System.out.print ("\t ");
                 System.out.print(df.format(sumRow[row]));
                 System.out.print ("\t \t ");
                 System.out.print(df.format(sumCol[row]));
                 System.out.println ();
                }  
                
                
                
//Calculates Ri+Ci 
       int RiLen,CiLen;
       RiLen= sumRow.length;
       CiLen =sumCol.length;
      if(RiLen==CiLen)
      {       for(row= 0; row < RiLen; row++)
               { 
                    for(col= 0; col < CiLen; col++)
                     {  
                      RiplusCi[row] = sumRow[row]+ sumCol[row];  
                     }  
            
                   
               } System.out.println ();
//Calculates  Ri -Ci 
        System.out.println ("       Ri+Ci         Ri-Ci:");
	    System.out.println ("---------------------------------------");
         
            for(row= 0; row < RiLen; row++)
               { 
                    for(col= 0; col < CiLen; col++)
                     {  
                      RiminusCi[row] = sumRow[row]- sumCol[row];  
                     }  
                
                }  
       
 // Print the Ri+Ci and Ri-Ci Values:
              for(row= 0; row < size; row++)
                { 
                 System.out.print ("\t ");
                 System.out.print(df.format(RiplusCi[row]));
                 System.out.print ("\t \t ");
                 System.out.print(df.format(RiminusCi[row]));
                 System.out.println ();
                }  
    }
     else
      { 
         System.out.println ("Cannot Calculate Ri+Ci and Ri-Ci ");
        
      }
       
            
 //close Main

 }


}


