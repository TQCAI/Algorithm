from structure import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not slow or not fast or not fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return True