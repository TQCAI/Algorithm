#include "bits/stdc++.h"

using namespace std;


class Solution {
public:
    string removeDuplicateLetters(string s) {
        deque<char> mono_stack;
        map<char, int> counter;
        set<char> stack_elements;
        for (char c:s) counter[c]++;
        for (char c:s) {
            if (!stack_elements.count(c)) { // c 不在栈中
                while (!mono_stack.empty() && mono_stack.back() > c &&
                       counter[mono_stack.back()] > 0) {
                    // fixme   ↑   写成了counter[c]
                    // counter[mono_stack.back()] > 0 ，而不是 > 1， 是因为 c 是当前字符
                    // counter 表示当前字符c之前的计数
                    // 如果把栈顶元素弄掉，就没了，所以不能这么做
                    stack_elements.erase(mono_stack.back());
                    mono_stack.pop_back();
                }
                stack_elements.insert(c);
                mono_stack.push_back(c);
            }
            counter[c]--;
        }
        string ans;
        for (char c:mono_stack) ans += c;
        return ans;
    }
};

int main() {
    cout << Solution().removeDuplicateLetters("cbacdcbc");
}