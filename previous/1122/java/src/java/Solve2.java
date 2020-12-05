import java.util.*;

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        List<Integer> arr2List=Arrays.asList(arr2);

    }
}


public class Solve2 {
    public static void main(String[] args) {
        int[] res = new Solution().relativeSortArray(
                new int[]{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19},
                new int[]{2, 1, 4, 3, 9, 6}
        );
        System.out.println(Arrays.toString(res));
    }
}
