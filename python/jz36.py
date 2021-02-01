from structure import TreeNode as Node


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        pre = None
        head = None

        def travel(node: Node):
            nonlocal pre, head
            if node is None:
                return
            travel(node.left)
            if head is None:
                # 不设dummy head
                head = node
            if pre is not None:
                pre.right = node
            node.left = pre
            pre = node
            travel(node.right)

        travel(root)
        pre.right = head
        head.left = pre
        return head


tree = Node(4, Node(2, Node(1), Node(3)), Node(5))
res = Solution().treeToDoublyList(tree)
print('test right')
k = 10
p = res
while k and p:
    k -= 1
    print(p.val)
    p = p.right
k = 10
p = res
print('test left')
while k and p:
    k -= 1
    print(p.val)
    p = p.left
