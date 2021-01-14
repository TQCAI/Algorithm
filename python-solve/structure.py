class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    @staticmethod
    def fromList(lst):
        head = None
        tail = None
        for item in lst:
            node = ListNode(item)
            if head is None:
                head = node
                tail = head
            else:
                tail.next = node
                tail = node
        return head

    def __str__(self):
        p = self
        res = ""
        while p is not None:
            res += f"{p.val} -> "
            p = p.next
        res += "O"
        return res

    __repr__ = __str__


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

    __repr__ = __str__


class UnionSet():
    def __init__(self, n):
        self.cnt = n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        self.parent[pa] = pb
        self.cnt -= 1

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        # 找到根节点
        r = x
        while r != self.parent[r]:
            r = self.parent[r]
        # 路径压缩
        while x != self.parent[x]:
            t = self.parent[x]
            self.parent[x] = r
            x = t
        return r
