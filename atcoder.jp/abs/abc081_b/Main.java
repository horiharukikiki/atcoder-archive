import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer a = Integer.parseInt(sc.next());
        int bit = 0;
        for (Integer i = 0; i < a; i++) {
            bit |= Integer.parseInt(sc.next());
        }
        System.out.println(Integer.numberOfTrailingZeros(bit));
    }
}