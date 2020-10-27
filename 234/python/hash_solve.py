from structure import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # hash = hash * seed + val
        # seed: prime number
        # val: node value
        # hash1 = a0 * seed^(n-1) + a1 * seed^(n-2)
        hash1 = hash2 = 0
        h = 1
        # seed=int(1e9+7)
        seed = 3
        p = head
        while p is not None:
            hash1 = hash1 * seed + p.val
            hash2 = hash2 + h * p.val
            h *= seed
            p = p.next
        return hash1 == hash2


if __name__ == '__main__':
    node = ListNode.fromList([1, 2, 2, 1])
    print(Solution().isPalindrome(node))
