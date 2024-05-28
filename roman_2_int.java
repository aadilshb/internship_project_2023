package project_alpha;
import java.util.Scanner;
public class roman_2_int {
	public static int Roman2Int(String s) {
		int sum=0;
		for(int i=0;i<s.length();i++) {
			char a=s.charAt(i);
			if(a=='M')
				sum+=1000;
			else if(a=='D')
				sum+=500;
			else if(a=='C')
				sum+=100;
			else if(a=='L')
				sum+=50;
			else if(a=='X')
				sum+=10;
			else if(a=='V')
				sum+=5;
			else if(a=='I')
				sum+=1;
			else
				return 0;
		}
		for (int i = 0; i < s.length() - 1; i++) {
            if ((s.charAt(i) == 'I' && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X'))
                || (s.charAt(i) == 'X' && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C'))
                || (s.charAt(i) == 'C' && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M'))) {
                sum -= 2 * value(s.charAt(i));
            }
        }

		return sum;
	}
	public static int value(char roman) {
        if (roman == 'M') return 1000;
        if (roman == 'D') return 500;
        if (roman == 'C') return 100;
        if (roman == 'L') return 50;
        if (roman == 'X') return 10;
        if (roman == 'V') return 5;
        if (roman == 'I') return 1;
        return 0;
    }
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Roman Number");
		String s=sc.nextLine();
		int k=Roman2Int(s);
		int f=0;
		for(int i=0;i<s.length();i++) {
			char a=s.charAt(i);
			if(Character.isDigit(a)||Character.isLowerCase(a))
				f=1;
		}
		if(f==1||k==0)
			System.out.println("Enter valid Roman Number!");
		else
			System.out.println("The integer value is : "+k);
		sc.close();
	}
}
