#include <bits/stdc++.h>

#define FF(a, b) for(int a=0;a<b;a++)
#define F(a, b) for(int a=1;a<=b;a++)
#define LEN 200
#define INF ((1<<30)-1)
#define bug(x) cout<<#x<<"="<<x<<endl;

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

int post[LEN] = {2, 6, 5, 9, 11, 10, 8};
int in[LEN] = {2, 5, 6, 8, 9, 10, 11};

BTNode *build_tree(int ps, int pe, int is, int ie) {
    if (ps > pe) return NULL;
    if (ps == pe) return new BTNode(in[is]);
    int i = is;
    while (i <= ie && in[i] != post[pe]) i++;
    BTNode *node = new BTNode(in[i]);
    int n_left = i - is;    //左侧元素数量
    node->left = build_tree(ps, ps + n_left - 1, is, is + n_left - 1);
    node->right = build_tree(ps + n_left, pe - 1, i + 1, ie);
    return node;
}

void preorder(BTNode *node) {
    if (node == nullptr) return;
    printf("%d, ", node->val);
    preorder(node->left);
    preorder(node->right);
}

void inorder(BTNode *node) {
    if (node == nullptr) return;
    inorder(node->left);
    printf("%d, ", node->val);
    inorder(node->right);
}

void postorder(BTNode *node) {
    if (node == nullptr) return;
    postorder(node->left);
    postorder(node->right);
    printf("%d, ", node->val);
}

int main() {
    system("chcp 65001");
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
    postorder(root);
    printf("\n");
    inorder(root);
    printf("\n");
    root->print();
    int n=7;
    BTNode *root_bd = build_tree(0, n - 1, 0, n - 1);
    root_bd->print();
    return 0;
}