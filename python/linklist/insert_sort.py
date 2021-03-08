class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy = ListNode(-inf)
        dummy.next = head
        tail = head
        p = head.next
        tail.next = None
        while p:
            aft = p.next
            if p.val >= tail.val:
                tail.next = p
                tail = p
                tail.next = None
            else:
                dp = dummy
                # 结束循环后，dp.next.val > p.val
                while dp.next and dp.next.val <= p.val:
                    dp = dp.next
                p.next = dp.next
                dp.next = p
            p = aft
        return dummy.next
