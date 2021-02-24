import heapq
from typing import List

from structure import ListNode


class MyNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        my_lists=[MyNode(node) for node in lists]
        heapq.heapify(my_lists)
        dummy = ListNode(0)
        p = dummy
        while my_lists:
            node = heapq.heappop(my_lists).node
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(my_lists, MyNode(node.next))
        p.next = None
        return dummy.next
