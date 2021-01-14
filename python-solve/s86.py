from structure import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        head1 = ListNode(0)
        p1 = head1
        head2 = ListNode(0)
        p2 = head2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        if head1.next is None:
            return head2.next
        if head2.next is None:
            return head1.next
        p1.next = head2.next
        p2.next = None
        return head1.next


res = Solution().partition(ListNode.fromList([1, 4, 3, 2, 5, 2]), 3)
print(res)
