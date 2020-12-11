package s23_2;

import structure.ListNode;

import java.util.PriorityQueue;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Status> queue = new PriorityQueue<>();
        for (ListNode node : lists) {
            if (node != null) {
                queue.offer(new Status(node.val, node));
            }
        }
        ListNode head = new ListNode(0);
        ListNode tail = head;
        while (!queue.isEmpty()) {
            Status f = queue.poll();
            tail.next = f.ptr;
            tail = tail.next;
            if (f.ptr.next != null) {
                queue.offer(new Status(f.ptr.next.val, f.ptr.next));
            }
        }
        return head.next;
    }

    class Status implements Comparable<Status> {
        int val;
        ListNode ptr;

        Status(int val, ListNode ptr) {
            this.val = val;
            this.ptr = ptr;
        }

        public int compareTo(Status status2) {
            return this.val - status2.val;
        }
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
