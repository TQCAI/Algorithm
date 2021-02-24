from structure import ListNode


def merge(h1: ListNode, h2: ListNode):
    p1, p2, dummy = h1, h2, ListNode(0)
    dp = dummy
    while p1 and p2:
        if p1.val < p2.val:
            dp.next = p1
            p1 = p1.next
        else:
            dp.next = p2
            p2 = p2.next
        dp = dp.next
    dp.next = p1 if p1 else p2
    return dummy.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        sub_len = 1
        while sub_len < length:
            pre, cur = dummy, dummy.next
            while cur:
                h1 = cur
                for _ in range(sub_len - 1):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                h2 = cur.next
                cur.next = None  # h1 结扎
                cur = h2         # 恢复 cur
                for _ in range(sub_len - 1):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                suc = None
                if cur:  # 构造新的【cur】
                    suc = cur.next
                    cur.next = None  # h2 结扎
                cur = suc  #
                merged = merge(h1, h2)
                pre.next = merged
                # 构造新的【pre】 (merged的最后一个结点)
                while pre.next:
                    pre = pre.next
            sub_len *= 2
        return dummy.next


print(Solution().sortList(ListNode.fromList([4, 2, 1, 3])))
#
# print(merge(ListNode.fromList([1, 3, 5]), ListNode.fromList([2, 4, 6, 7])))
