import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.Arrays;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    static ListNode fromList(@NotNull ArrayList<Integer> list) {
        ListNode head = null;
        ListNode tail = null;
        for (Integer item : list) {
            ListNode node = new ListNode(item);
            if (head == null) {
                head = node;
                tail = node;
            } else {
                tail.next = node;
                tail = node;
            }
        }
        return head;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        ListNode p = this;
        while (p != null) {
            res.append(p.val).append(" -> ");
            p = p.next;
        }
        res.append("O");
        return res.toString();
    }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        return new ListNode();
    }
}

public class Solve1 {
    public static void main(String[] args) {
        ListNode node=ListNode.fromList((ArrayList<Integer>) Arrays.asList(new Integer[]{1,2,3}));
        System.out.println(node);
    }
}
