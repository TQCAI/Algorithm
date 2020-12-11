package s493;

class Solution {
    public int reversePairs(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        return reversePairsRecursive(nums, 0, nums.length - 1);
    }

    public int reversePairsRecursive(int[] nums, int left, int right) {
        if (left == right) {
            return 0;
        } else {
            int mid = (left + right) / 2;
            int n1 = reversePairsRecursive(nums, left, mid);
            int n2 = reversePairsRecursive(nums, mid + 1, right);
            int ret = n1 + n2;

            // 首先统计下标对的数量
            int i = left;
            int j = mid + 1;
            while (i <= mid) {
                while (j <= right && (long) nums[i] > 2 * (long) nums[j]) {
                    j++;    // 右式判断满足题设条件
                }
                ret += j - mid - 1;  // 满足题设的数字 数， j不会清零，会累加
                i++; //i增加后，j不会清零，因为单调递增导致 nums[i] > 2 nums[j]
            }

            // 随后合并两个排序数组
            int[] sorted = new int[right - left + 1];
            int p1 = left, p2 = mid + 1;
            int p = 0;
            while (p1 <= mid && p2 <= right) {
                if (nums[p1] < nums[p2]) {
                    sorted[p++] = nums[p1++];
                } else {
                    sorted[p++] = nums[p2++];
                }
            }
            while (p1 <= mid) sorted[p++] = nums[p1++];
            while (p2 <= right) sorted[p++] = nums[p2++];
            for (int k = 0; k < sorted.length; k++) {
                nums[left + k] = sorted[k];
            }
            return ret;
        }
    }
}

public class S493 {
    public static void main(String[] args) {
        int ret = new Solution().reversePairs(new int[]{1, 3, 2, 3, 1});
        System.out.println(ret);
    }
}

