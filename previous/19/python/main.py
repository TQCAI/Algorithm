from structure import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        k = 0
        p2 = None
        while p is not None:
            p = p.next
            k += 1
            if (k - 1) == n:
                p2 = head
            if (k - 1) > n:
                p2 = p2.next
        if p2 is None and k == n:
            head = head.next
        elif p2.next is not None:
            p2.next = p2.next.next
        return head


if __name__ == '__main__':
    node = Solution().removeNthFromEnd(ListNode.fromList([1, 2]), 2)
    print(node)
