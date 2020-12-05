from structure import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:  # 用例 []
            return None
        odds = None
        evens = None
        index = 1
        p = head
        evens_head = None
        while p is not None:
            if index % 2:
                if odds is not None:
                    odds.next = p
                odds = p
            else:
                if evens is not None:
                    evens.next = p
                else:
                    evens_head = p
                evens = p
            p = p.next
            index += 1
        if evens is not None:  # 用例 [1]
            evens.next = None  # 注意了
        odds.next = evens_head
        return head


if __name__ == '__main__':
    nodes = ListNode.fromList([1, 2, 3, 4, 5])
    solved = Solution().oddEvenList(nodes)
    print(solved)
