[剑指 Offer 58 - I. 翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)

[面试题58 - I. 翻转单词顺序（双指针 / 库函数，清晰图解）](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/solution/mian-shi-ti-58-i-fan-zhuan-dan-ci-shun-xu-shuang-z/)

一行Python

```python
return " ".join(reversed(s.split()))
```

- 双指针

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        ret = []
        while i >= 0:
            # 找到开头或单词前的空格
            while i >= 0 and s[i] != ' ':
                i -= 1
            ret.append(s[i + 1:j + 1])
            # 跳过空格
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i
        return " ".join(ret)
```

- 手写split

TODO