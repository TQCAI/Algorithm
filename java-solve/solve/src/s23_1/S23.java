package s23_1;

import structure.ListNode;

class Solution {
    public ListNode mergeTwoLists(ListNode a, ListNode b) {
        if (a == null || b == null) {
            return a != null ? a : b;
        }
        ListNode head = new ListNode(0);
        ListNode tail = head, aPtr = a, bPtr = b;
        while (aPtr != null && bPtr != null) {
            if (aPtr.val < bPtr.val) {
                tail.next = aPtr;
                aPtr = aPtr.next;
            } else {
                tail.next = bPtr;
                bPtr = bPtr.next;
            }
            tail = tail.next;
        }
        tail.next = (aPtr != null ? aPtr : bPtr);
        return head.next;
    }

    public ListNode merge(ListNode[] lists, int l, int r) {
        if (l == r) {
            return lists[l];
        }
        if (l > r) {
            return null;
        }
        int mid = (l + r) >> 1;
        return mergeTwoLists(
                merge(lists, l, mid),
                merge(lists, mid + 1, r)
        );
    }

    public ListNode mergeKLists(ListNode[] lists) {
        return merge(lists, 0, lists.length - 1);
    }
}

public class S23 {
    public static void main(String[] args) {
        System.out.println(new Solution().mergeKLists(
                new ListNode[]{
                        ListNode.fromArray(new int[]{1, 4, 5}),
                        ListNode.fromArray(new int[]{1, 3, 4}),
                        ListNode.fromArray(new int[]{2, 6}),
                }
        ));
    }
}
