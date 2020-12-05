import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        p = head
        while p is not None:
            nodes.append(p)
            pre = p
            p = p.next
            pre.next = None
        N = len(nodes)
        mid = math.floor(len(nodes) / 2)
        list2 = list(reversed(nodes[mid:]))
        list1 = nodes[:mid]
        if len(list2) > len(list1):
            list1.append(list2.pop())
        lst = [list1, list2]
        for i in range(N):
            if i == 0:
                head = list1[0]
                p = head
            else:
                p.next = lst[i % 2][i // 2]
                p = p.next


if __name__ == '__main__':
    head = ListNode.fromList([1, 2, 3, 4, 5])
    Solution().reorderList(head)
    print(head)
