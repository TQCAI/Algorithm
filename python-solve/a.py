class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        res = ListNode(0)
        p = res
        while p1 and p2:
            if p1.val < p2.val:
                cp = p1
                p1 = p1.next  # 写后面无效
            else:
                cp = p2
                p2 = p2.next
            p.next = cp
            p = p.next
        p.next = p1 if p1 else p2
        return res.next
