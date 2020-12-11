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

int pre[LEN] = {8, 5, 2, 6, 10, 9, 11};
int in[LEN];
int post[LEN] = {2, 6, 5, 9, 11, 10, 8};
int t = 0;
int flag = 1;

void setIn(int preS, int preE, int postS, int postE) {
    if (preS == preE) {
        in[t++] = pre[preS];
        return;
    }
    //finding the elem which is the root of left sub_tree
    int i = postS;
    while (i <= postE && post[i] != pre[preS + 1]) i++;
    //calculate the numbers of left sub_tree
    int leftNum = i - postS + 1;
    //is paradox
    if (i == postE - 1) {
        flag = 0;
        setIn(preS + 1, preS + leftNum, postS, i);//default consider this is a right leaf
        in[t++] = pre[preS];
        return;
    }
    //build the in_order traversal sequence
    setIn(preS + 1, preS + leftNum, postS, i);
    in[t++] = pre[preS];
    setIn(preS + leftNum + 1, preE, i + 1, postE - 1);
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
    preorder(root);
    printf("\n");
    postorder(root);
    printf("\n");
    root->print();
    int n = 7;
    t = 0;
    setIn(0, n - 1, 0, n - 1);
    for (int i = 0; i < n; ++i) {
        printf("%d, ", in[i]);
    }
    printf("\n");
    inorder(root);
    bug(flag)
    return 0;
}