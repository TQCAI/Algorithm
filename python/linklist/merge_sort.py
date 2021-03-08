from structure import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归终点
        if not head or not head.next:
            return head
        # 中点寻找
        slow = head
        fast = head.next  # 否则爆栈
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        # 处理左链表与右链表
        left = self.sortList(head)
        right = self.sortList(mid)
        # 合并两个排序连败哦
        dummy = dp = ListNode(0)
        while left and right:
            if left.val < right.val:
                dp.next = left
                left = left.next
            else:
                dp.next = right
                right = right.next
            dp = dp.next
        dp.next = left if left else right
        return dummy.next


ans = Solution().sortList(ListNode.fromList([1, 5, 3, 4, 0]))
print(ans)
