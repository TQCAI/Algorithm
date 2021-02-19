class Solution:
    def reverse(self, a, b):
        # 相当于左开右闭，例如k=2,
        #  1->2->3
        # a↑    b↑
        # 最后返回是的 2->1->∅
        pre = None
        p = a
        while p != b:
            aft = p.next
            p.next = pre
            pre = p
            p = aft
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        a = b = head
        # 循环体写错 (老错误)
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        new_head = self.reverse(a, b)
        # 把 a 写成了 new_head
        a.next = self.reverseKGroup(b, k) # b 写错 (老错误)
        return new_head
