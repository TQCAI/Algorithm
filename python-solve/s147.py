from structure import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next
        while curr:
            # 排序区最后的元素小于等于当前元素，把当前元素放排序区后面就行
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            # 否则
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                # prev.next.val > curr.val
                # prev.val <= curr.val
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next
        return dummyHead.next
