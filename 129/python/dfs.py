# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    sum_list = []

    def dfs(self, node, sum):
        if node is not None:
            cur_sum = sum + str(node.val)
            self.dfs(node.left, cur_sum)
            self.dfs(node.right, cur_sum)
            if node.left is None and node.right is None:
                self.sum_list.append(cur_sum)

    def sumNumbers(self, root: TreeNode) -> int:
        self.sum_list = []
        self.dfs(root, "")
        return sum(map(int, self.sum_list))

def case1():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    res = Solution().sumNumbers(tree)
    print(res)

def case2():
    tree = TreeNode(4)
    tree.left = TreeNode(9)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)
    tree.right = TreeNode(0)
    res = Solution().sumNumbers(tree)
    print(res)

case2()