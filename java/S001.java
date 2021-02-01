import java.util.Arrays;
import java.util.HashMap;


class Solution_S001 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int sub = target - num;
            if (hashMap.containsKey(sub)) {
                return new int[]{i, hashMap.get(sub)};
            }
            hashMap.put(num, i);
        }
        return new int[]{0, 0};
    }
}

public class S001 {

    public static void main(String[] args) {
        int[] ret = new Solution_S001().twoSum(new int[]{2, 7, 11, 15}, 9);
        System.out.println(Arrays.toString(ret));
    }
}
