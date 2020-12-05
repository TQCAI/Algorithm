#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
from structure import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        oddHead, evenHead = head, head.next
        odd, even = oddHead, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next         # 别忘了自己要移动
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


if __name__ == '__main__':
    nodes = ListNode.fromList([1, 2, 3, 4, 5])
    solved = Solution().oddEvenList(nodes)
    print(solved)
