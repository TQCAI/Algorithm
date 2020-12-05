from structure import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                # 构造 head1
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                # 构造 head2
                head2 = curr.next
                curr.next = None  # head1 结尾为空
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                # 将curr指向下一个节点，并让head2 结尾为空
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                curr = succ
                # 合并两个有序链表
                merged = merge(head1, head2)
                # 套到上一个节点上
                prev.next = merged
                # 构造新的prev
                while prev.next:
                    prev = prev.next
            subLength *= 2

        return dummyHead.next


print(Solution().sortList(ListNode.fromList([-1, 5, 3, 4, 0])))
