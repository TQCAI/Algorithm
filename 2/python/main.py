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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        ret = None
        p = None
        carry = 0
        while p1 is not None or p2 is not None:
            v1 = p1.val if p1 is not None else 0
            v2 = p2.val if p2 is not None else 0
            num = v1 + v2 + carry
            node = ListNode(num % 10)
            carry = num // 10
            if ret is None:
                ret = node
                p = ret
            else:
                p.next = node
                p = p.next
            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None
        return ret

ret=Solution().addTwoNumbers(ListNode.fromList([2,4,3]), ListNode.fromList([5,6,4]))
print(ret)
