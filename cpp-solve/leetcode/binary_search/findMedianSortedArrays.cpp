#include "bits/stdc++.h"

using namespace std;

// todo: 有空二刷一遍

class Solution {
public:
    int findKthElement(vector<int> &nums1, vector<int> &nums2, int k) {
        int index1 = 0;
        int index2 = 0;
        int l1 = nums1.size(), l2 = nums2.size();
        while (true) {
            if (index1 == l1)
                return nums2[index2 + k - 1];
            if (index2 == l2)
                return nums1[index1 + k - 1];
            if (k == 1)
                return min(nums1[index1 + k - 1], nums2[index2 + k - 1]);
            int ix1 = min(l1 - 1, index1 + k / 2 - 1); // 忘了 /2 ，debug看出来的
            int ix2 = min(l2 - 1, index2 + k / 2 - 1);
            if (nums1[ix1] < nums2[ix2]) {
                k -= ix1 + 1 - index1;
                index1 = ix1 + 1;
            } else {
                k -= ix2 + 1 - index2;
                index2 = ix2 + 1;
            }
        }
    }

    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        int total_len = nums1.size() + nums2.size();
        if (total_len % 2 == 1)
            return findKthElement(nums1, nums2, total_len / 2 + 1);
        else
            return double(findKthElement(nums1, nums2, total_len / 2) +
                          findKthElement(nums1, nums2, total_len / 2 + 1)) / 2;
    }
};

int main() {
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    int ans = Solution().findMedianSortedArrays(nums1, nums2);
    cout << ans << endl;
}