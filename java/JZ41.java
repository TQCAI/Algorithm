import java.util.PriorityQueue;

class MedianFinder {

    PriorityQueue<Integer> lo;
    PriorityQueue<Integer> hi;

    /**
     * initialize your data structure here.
     */
    public MedianFinder() {
        // 大根堆
        lo = new PriorityQueue<>((a, b) -> {
            return b - a;
        });
        hi = new PriorityQueue<>();
    }

    public void addNum(int num) {
        lo.offer(num);
        hi.offer(lo.poll());
        if (lo.size() < hi.size())
            lo.offer(hi.poll());
    }

    public double findMedian() {
        return lo.size() == hi.size() ? (lo.peek() + hi.peek()) / 2.0 : lo.peek();
    }
}

public class JZ41 {
}
