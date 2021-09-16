import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        String[] numbers = s.split("");
        int cnt = 0;

        for (int i = 0; i < s.length(); i++){
            if (numbers[i].equals("1")){
                cnt += 1;
            }
        }
        System.out.println(cnt);
        scan.close();
    }
}