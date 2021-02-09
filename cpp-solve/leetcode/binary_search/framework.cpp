#include "bits/stdc++.h"

using namespace std;

vector<int> nums = {1, 1, 3, 6, 6, 6, 7, 8, 8, 9};

int binary_search(vector<int> nums, int target) {
    int l = 0, r = nums.size() - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] == target)
            return mid;
        if (nums[mid] < target)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return -1;
}

int lower_bound(vector<int> nums, int target) {
    int l = 0, r = nums.size();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] == target)
            r = mid;
        else if (nums[mid] < target)
            l = mid + 1;
        else
            r = mid;
    }
    if (l == nums.size())
        return -1;
    return nums[l] == target ? l : -1;
}

int upper_bound(vector<int> nums, int target) {
    int l = 0, r = nums.size();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] == target)
            l = mid + 1;
        else if (nums[mid] < target)
            l = mid + 1;
        else
            r = mid;
    }
    if (l == 0)
        return -1;
    return nums[l - 1] == target ? l - 1 : -1;
}

int main() {
    cout << binary_search(nums, 6) << endl;
    cout << lower_bound(nums, 6) << endl;
    cout << upper_bound(nums, 6) << endl;
}