#include "bits/stdc++.h"

using namespace std;

class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        map<int,int> counter;
        int ans=0;
        for(auto a:A)
            for(auto b:B)
                counter[a + b]+=1;
        for(auto c:C)
            for(auto d:D){
                int target = -(c + d);
                if(counter.count(target))
                    ans += counter[target];
            }
        return ans;
    }
};

int main() {
    vector<int> nums = {1, 0, -1, 0, -2, 2};
    vector<vector<int>> ans = Solution().fourSum(nums, 0);
    cout << ans.size();
}