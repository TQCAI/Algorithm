#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const double pi = acos(-1);

class BTNode {
public:
    int val;
    BTNode *left;
    BTNode *right;

    BTNode() {
        this->left = nullptr;
        this->right = nullptr;
        val = -1;
    };

    BTNode(int val) {
        this->left = nullptr;
        this->right = nullptr;
        this->val = val;
    };

    BTNode(int val, BTNode *left, BTNode *right) {
        this->left = left;
        this->right = right;
        this->val = val;
    };

    void printBT(const std::string &prefix, const BTNode *node, bool isLeft) {
        if (node != nullptr) {
            std::cout << prefix;

            std::cout << (isLeft ? "├──" : "└──");

            // print the value of the node
            std::cout << node->val << std::endl;

            // enter the next tree level - left and right branch
            printBT(prefix + (isLeft ? "│   " : "    "), node->left, true);
            printBT(prefix + (isLeft ? "│   " : "    "), node->right, false);
        }
    }

    void print() {
        printBT("", this, false);
    }
};


int main() {
    // 控制台显示乱码纠正
    system("chcp 65001"); //设置字符集 （使用SetConsoleCP(65001)设置无效，原因未知）
    // pass the root node of your binary tree
    BTNode *root = new BTNode(
            8,
            new BTNode(
                    5,
                    new BTNode(2),
                    new BTNode(6)
            ),
            new BTNode(
                    10,
                    new BTNode(9),
                    new BTNode(11)
            )
    );
    root->print();
    return 0;
}