from structure import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None
        dummy = ListNode()
        dp = dummy
        p = head
        while p:
            np = p.next
            if np:
                nnp = np.next
                dp.next = np
                dp = dp.next
                dp.next = p
                dp = dp.next
                p = nnp
            else:
                dp.next = p
                dp=dp.next
                break
        if dp:
            dp.next = None
        return dummy.next


print(Solution().swapPairs(ListNode.fromList([1])))
