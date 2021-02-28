class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverse(self, a, b):
        p = a
        pre = None
        while p != b:
            aft = p.next
            p.next = pre
            pre = p
            p = aft
        return pre

    def reverseKGroup(self, head, k):
        a = b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        n_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return n_head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
p = Solution().reverseKGroup(head, 1)
while p:
    print(p.val)
    p = p.next
