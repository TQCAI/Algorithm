from structure import ListNode


class Solution:
    def recurse(self, head: ListNode):
        #                     写错↓
        if head is None or head.next is None:
            return head  # ←写错
        last = self.recurse(head.next)
        head.next.next = head
        head.next = None
        return last

    successor = None

    def recurseN(self, head: ListNode, n: int):
        if n == 1:
            self.successor = head.next
            return head
        last = self.recurseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.recurseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head


node = ListNode.fromList([1, 2, 3, 4, 5])
print(Solution().recurse(node))
node = ListNode.fromList([1, 2, 3, 4, 5])
print(Solution().recurseN(node, 2))
node = ListNode.fromList([1, 2, 3, 4, 5])
print(Solution().reverseBetween(node, 2, 4))
