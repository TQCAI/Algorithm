package design;

import java.util.HashMap;

class Node {
    int k, v;
    Node next = null;
    Node prev = null;

    Node(int k, int v) {
        this.k = k;
        this.v = v;
    }
}

class DoubleLink {
    int size;
    Node head, tail;

    DoubleLink() {
        size = 0;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail; // fixme : 注意初始化
        tail.prev = head;
    }

    Node remove(Node x) {
        x.next.prev = x.prev;
        x.prev.next = x.next;
        size--;
        return x;
    }

    void addLast(Node x) {
        x.prev = tail.prev;
        tail.prev.next = x;
        x.next = tail;
        tail.prev = x;
        size++;
    }

    Node removeFirst() {
        return remove(head.next);
    }
}

class LRU {
    int capacity;
    HashMap<Integer, Node> cache;
    DoubleLink link;

    LRU(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();
        link = new DoubleLink();
    }

    int get(int k) {
        if (cache.containsKey(k))
            return makeRecently(k);
        return -1;

    }

    void put(int k, int v) {
        if (cache.containsKey(k)) {
            removeKey(k);
            addRecently(k, v);
        } else {
            if (cache.size() >= capacity) {
                removeLeastRecently();
            }
            addRecently(k, v);
        }
    }

    int makeRecently(int k) {
        Node node = cache.get(k);
        link.addLast(link.remove(node));
        return node.v;
    }

    void addRecently(int k, int v) {
        Node node = new Node(k, v);
        cache.put(k, node);
        link.addLast(node);
    }

    void removeKey(int k) {
        Node node = cache.get(k);
        link.remove(node);
    }

    void removeLeastRecently() {
        Node oldestNode = link.removeFirst();
        cache.remove(oldestNode);
    }
}

public class Main {
    public static void main(String[] args) {
        LRU lru = new LRU(2);
        lru.put(1, 1);
        lru.put(2, 2);
        lru.get(1);
    }
}
