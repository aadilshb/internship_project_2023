package project_alpha;
import java.util.*;
public class matrix_zero {
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Number of Rows?");
		int m=sc.nextInt();
		System.out.println("Number of Columns?");
		int n=sc.nextInt();
		System.out.println("Enter the matrix");
		int[][] mat=new int[m][n];
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				mat[i][j]=sc.nextInt();
		for(int i=0;i<m;i++) {
			for(int j=0;j<n;j++) {
				if(mat[i][j]==0) {
					for(int k=0;k<m;k++)
						if(mat[k][j]!=0)
							mat[k][j]=-232;
					for(int k=0;k<n;k++)
						if(mat[i][k]!=0)
							mat[i][k]=-232;
				}
			}
		}
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (mat[i][j] == -232)
	                    mat[i][j] = 0;
		System.out.println("The matrix is: ");
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++) {
				System.out.print(mat[i][j]+"  ");
				if(j==n-1)
					System.out.println();
			}
	}
}
