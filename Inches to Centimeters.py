import java.util.Scanner;
public class InchesInCentimeters{
    public static void main (String[] args){
        Scanner sc=new Scanner(System.in);
        int heightInInches=sc.nextInt();
        double heightInCm=heightInInches*2.54;
        System.out.printf("%.2f",heightInCm);
    }
}