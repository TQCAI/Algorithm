[剑指 Offer 65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

[面试题65. 不用加减乘除做加法（位运算，清晰图解）](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/)

```java
class Solution {
    public int add(int a, int b) {
        int c;
        while (b != 0) {  // 条件需要是 !=0 ，而不是 > 0
            c = (a & b) << 1;
            a ^= b;
            b = c;
        }
        return a;
    }
}
```


