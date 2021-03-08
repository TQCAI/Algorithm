from structure import ListNode


def reverse(a, b):
    pre = None
    p = a
    while p != b:
        aft = p.next
        p.next = pre
        pre = p
        p = aft
    return pre


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        a = head
        b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        n_head = reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return n_head


ans = Solution().reverseKGroup(ListNode.fromList([1, 2, 3, 4, 5]), 2)
print(ans)
