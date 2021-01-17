from structure import ListNode


class Solution:
    def traverse(self, right):
        if right is None:
            return True
        ans = self.traverse(right.next)
        ans &= (self.left.val == right.val)
        self.left = self.left.next
        return ans

    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)
