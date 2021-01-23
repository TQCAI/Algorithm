package s295;

import java.util.PriorityQueue;

class MedianFinder {
    PriorityQueue<Integer> lo;
    PriorityQueue<Integer> hi;

    public MedianFinder() {
        // 较小数字，大根堆
        lo = new PriorityQueue<Integer>((a, b) -> {
            return b - a;
        });
        // 较大数字， 小跟对
        hi = new PriorityQueue<Integer>();
    }

    public double findMedian() {
        return lo.size() == hi.size() ? (lo.peek() + hi.peek()) / 2.0 : lo.peek();
    }

    public void addNum(int num) {
        // 我的理解，数字从小到大，先丢到lo
        lo.offer(num);
        // 然后升到hi，平衡操作
        hi.offer(lo.poll());
        // 面向记忆刷题的话，下面的操作和上面是反过来的。
        // lo 必然要比 hi 元素多，所以判断条件和这个事实反过来
        if (lo.size() < hi.size()) {
            lo.offer(hi.poll());
        }
    }
}

public class S295 {
}
