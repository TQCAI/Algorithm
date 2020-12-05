from structure import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None
        p = head
        vec = []
        while p is not None:
            vec.append(p)
            p = p.next
        i = 0
        j = len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None  # 容易想错


node = ListNode.fromList([1, 2, 3, 4])
Solution().reorderList(node)
print(node)

node = ListNode.fromList([1, 2, 3, 4, 5])
Solution().reorderList(node)
print(node)
