package solve1;

import java.util.*;

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> counter = new HashMap<>();
        int[] res = new int[arr1.length];
        int idx = 0;
        for (int i : arr1) {
            counter.merge(i, 1, Integer::sum);
        }
        for (int e : arr2) {
            if (counter.containsKey(e)) {
                int cnt = counter.get(e);
                for (int j = 0; j < cnt; j++) {
                    res[idx] = e;
                    idx += 1;
                }
                counter.remove(e);
            }
        }
        Set<Integer> setKey = counter.keySet();
        TreeSet<Integer> sortedKey = new TreeSet<>(setKey);
        for (int e : sortedKey) {
            int cnt = counter.get(e);
            for (int j = 0; j < cnt; j++) {
                res[idx] = e;
                idx += 1;
            }
        }
        return res;
    }
}

public class Solve1 {
    public static void main(String[] args) {
        int[] res = new Solution().relativeSortArray(
                new int[]{2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19},
                new int[]{2, 1, 4, 3, 9, 6}
        );
        System.out.println(Arrays.toString(res));
    }
}
