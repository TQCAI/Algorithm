from structure import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node


print(Solution().reverseList(ListNode.fromList([1, 2, 3, 4, 5])))
