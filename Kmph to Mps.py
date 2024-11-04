import java.util.Scanner;
public class KmphToMps{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int speedinKmph=sc.nextInt();
        double speedinMps=speedinKmph/3.6;
        System.out.printf("%.2f\n",speedinMps);
    }
}