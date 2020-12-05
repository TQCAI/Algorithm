import java.util.Arrays;

public class RadixSort {

    static int[] radixSort(int[] nums) {
        long exp = 1;
        int n = nums.length;
        int[] buf = new int[n];
        int maxVal = Arrays.stream(nums).max().getAsInt();
        while (maxVal >= exp) {
            int[] cnt = new int[10];
            for (int i = 0; i < n; i++) {
                int digit = (nums[i] / (int) exp) % 10;
                cnt[digit]++;
            }
            for (int i = 1; i < 10; i++) {  // cumulation
                cnt[i] += cnt[i - 1];
            }
            // 因为cnt维护索引是随迭代递减的，所以为了维护相对顺序，i也需要递减遍历
            for (int i = n - 1; i >= 0; i--) {
                int digit = (nums[i] / (int) exp) % 10;
                buf[cnt[digit] - 1] = nums[i];//计数-1=索引
                cnt[digit]--;
            }
            // src srcPos  dest  destPos  length
            System.arraycopy(buf, 0, nums, 0, n);
            exp *= 10;
        }
        return nums;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(RadixSort.radixSort(new int[]{
                334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424})));
    }
}
