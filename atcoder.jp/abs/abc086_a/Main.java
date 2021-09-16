import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner Scan = new Scanner(System.in);
        int a = Scan.nextInt();
        int b = Scan.nextInt();
        int num = a*b;
        if (num%2==0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }
        Scan.close();
    }
}