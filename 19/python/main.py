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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        k = 0
        p2 = None
        while p is not None:
            p = p.next
            k += 1
            if (k - 1) == n:
                p2 = head
            if (k - 1) > n:
                p2 = p2.next
        if p2 is None and k == n:
            head = head.next
        elif p2.next is not None:
            p2.next = p2.next.next
        return head


if __name__ == '__main__':
    node = Solution().removeNthFromEnd(ListNode.fromList([1, 2]), 2)
    print(node)
