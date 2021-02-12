#include "bits/stdc++.h"
#include "vector_util.h"

using namespace std;


class Solution {
public:
    vector<int> getMaxK(vector<int> &nums, int k) {
        // 单调栈，单调递增
        int m = nums.size() - k; // 最多能删掉的元素
        vector<int> mono_stack;
        for (int num:nums) {
            if (!mono_stack.empty() && mono_stack.back() < num && m > 0) {
                m--;
                mono_stack.pop_back();
            }
            mono_stack.push_back(num);
        }
        // 如果是单调递减序列，需要截断
        return vector<int>(mono_stack.begin(), mono_stack.begin() + k);
    }

    vector<int> maxNumber(vector<int> &nums1, vector<int> &nums2, int k) {
        vector<int> ans(k, -99999);
        for (int i = 0; i <= k; ++i) {
            int j = k - i;
            if (i > nums1.size() || j > nums2.size())
                continue;
            vector<int> v1 = getMaxK(nums1, i);
            vector<int> v2 = getMaxK(nums2, j);
            vector<int> cur_vec = merge(v1, v2);
            if (greater_than(cur_vec, ans))  // cur_vec > ans
                ans = cur_vec;
            cout << vector2str(cur_vec) << endl;
        }
        return ans;
    }

    vector<int> merge(vector<int> &v1, vector<int> &v2) {
        vector<int> ans(v1.size() + v2.size(), 0);
        int i = 0, j = 0, k = 0;
        while (i < v1.size() && j < v2.size()) {
            if (v1[i] > v2[j]) {
                ans[k++] = v1[i++];
            } else if (v1[i] < v2[j]) {
                ans[k++] = v2[j++];
            } else {
                // 为的是解决 [6, 7], [6, 0, 4] 这样的case
                int num1 = (i == v1.size() - 1) ? v1[i] : v1[i + 1];
                int num2 = (j == v2.size() - 1) ? v2[j] : v2[j + 1];
                if (num1 > num2) ans[k++] = v1[i++];
                else ans[k++] = v2[j++];
            }
        }
        while (i < v1.size()) ans[k++] = v1[i++];
        while (j < v2.size()) ans[k++] = v2[j++];
        return ans;
    }

    bool greater_than(vector<int> &v1, vector<int> &v2) {
        for (int i = 0; i < v1.size(); ++i) {
            if (v1[i] > v2[i])
                return true;
            else if (v1[i] < v2[i])  // fixme: 要加这行，我人没了
                return false;
        }
        return false;
    }
};

int main() {
    vector<int> v = {9, 8, 7, 6};
    vector<int> ans = Solution().getMaxK(v, 3);
    cout << vector2str(ans) << endl;
    cout << ans.size() << endl;
    vector<int> v1 = {6, 7};
    vector<int> v2 = {6, 0, 4};
    vector<int> a2 = Solution().maxNumber(v1, v2, 5);
    cout << vector2str(a2);
}