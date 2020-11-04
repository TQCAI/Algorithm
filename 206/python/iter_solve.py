from structure import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        p = head
        while p is not None:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre

print(Solution().reverseList(ListNode.fromList([1,2,3,4,5])))
