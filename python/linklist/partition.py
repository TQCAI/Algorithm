from structure import ListNode

node = ListNode.fromList([1, 2])


def partition(head: ListNode):
    if not head or not head.next:
        return head
    p1, p2 = head, head.next
    head1, head2 = p1, p2
    # p2 后面至少有1个结点
    while p2 and p2.next:
        p1.next = p2.next
        p1 = p1.next
        p2.next = p1.next
        p2 = p2.next
    p1.next = None
    return head1, head2


print(partition(node))
