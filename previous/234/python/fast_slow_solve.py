from structure import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pre = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        if fast is not None:
            slow = slow.next
        while slow is not None:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True


if __name__ == '__main__':
    node = ListNode.fromList([1, 2, 2, 1])
    print(Solution().isPalindrome(node))
