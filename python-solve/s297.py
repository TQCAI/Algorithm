from structure import TreeNode


class Codec:
    NULL = '#'

    def serialize(self, root: TreeNode) -> str:
        res = []

        def traverse(root: TreeNode):
            if root is None:
                res.append(self.NULL)
            else:
                res.append(str(root.val))
                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        lst = data.split(',')

        def traverse():
            val = lst.pop(0)
            if val == self.NULL:
                return None
            else:
                node = TreeNode(int(val))
                node.left = traverse()
                node.right = traverse()
                return node

        return traverse()
