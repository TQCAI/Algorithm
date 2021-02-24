from math import inf

from structure import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy = ListNode(-inf) # D
        dummy.next = head  # D 4 2 1 3 ∅
        tail = dummy.next  # 4 ∅ // 如果新结点比【有序区】的【尾结点】更大，直接成为新的尾结点
        p = head.next      # 2 1 3 ∅ // 头结点的第一个元素初始为【有序区】，从头结点的【下一个元素】开始遍历
        tail.next = None   # 封闭有序区
        while p:
            aft = p.next # 缓存下一个结点
            if p.val >= tail.val:  # 注意符号
                tail.next = p
                tail = p
            else:
                dp = dummy
                while dp.next:
                    # 首次出现比p大的元素。插入到那个元素前面
                    if dp.next.val > p.val:
                        p.next = dp.next
                        dp.next = p
                        break
                    dp=dp.next
            p = aft
            tail.next = None
        return dummy.next



head = ListNode.fromList([4, 2, 1, 3])
ans = Solution().insertionSortList(head)
print(ans)
