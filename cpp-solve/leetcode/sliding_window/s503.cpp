#include "bits/stdc++.h"
#include "vector_util.h"

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int> &nums) {
        vector<int> mono_stack;
        map<int, int> next_bigger;
        int n = nums.size();
        vector<int> ans(n);
        for (int i = n * 2 - 1; i >= 0; --i) {
            int num = nums[i % n];  //              fixme:  ↓
            while (!mono_stack.empty() && mono_stack.back() <= num) {
                mono_stack.pop_back();
            }
            ans[i % n] = mono_stack.empty() ? -1 : mono_stack.back();
            mono_stack.push_back(num);
        }
        return ans;
    }
};

int main() {
    vector<int> nums1 = {4, 1, 2}, nums2 = {1, 3, 4, 2};
    vector<int> ans = Solution().nextGreaterElement(
            nums1, nums2
    );
    cout << ans.size();
}