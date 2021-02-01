from structure import TreeNode

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        lst = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)

        inorder(root)
        lst.sort()
        index = 0

        def inorder2(root):
            nonlocal index
            if not root:
                return
            inorder2(root.left)
            root.val = lst[index]
            index += 1
            inorder2(root.right)

        inorder2(root)


res=Solution().recoverTree(TreeNode(1,TreeNode(3,None,TreeNode(2))))
print(res)