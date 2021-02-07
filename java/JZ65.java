class Solution {
    public int add(int a, int b) {
        int c;
        while (b != 0) {  // 条件需要是 !=0 ，而不是 > 0
            c = (a & b) << 1;
            a ^= b;
            b = c;
        }
        return a;
    }
}

public class JZ65 {
    public static void main(String[] args) {
        System.out.println();
    }
}
