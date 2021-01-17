from structure import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p = head
        res = ListNode(0)
        p_res = res
        for _ in range(m - 1):
            p_res.next = p
            p_res = p_res.next
            p = p.next
        pp = None
        idx = 0
        p2 = p
        while p and idx < (n - m + 1):
            idx += 1
            next = p.next
            p.next = pp
            pp = p
            p = next
        if p2:
            p2.next = p
        p_res.next = pp
        return res.next


node = ListNode.fromList([1, 2, 3, 4, 5])
print(Solution().reverseBetween(node, 2, 4))
