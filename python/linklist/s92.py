from structure import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 以case 1, 2, 3, 4, 5 为例，left = 2, right = 4
        p = head
        L = right - left + 1 # 翻转的部分是 2 3 4， 长度为3
        dummy=ListNode(0)
        dp=dummy
        for _ in range(left - 1): # 把 翻转部分 2 之前的添加到dummy中（dummy用来返回）
            dp.next=p
            dp=dp.next
            p = p.next
        # 迭代完之后 p=2
        aft = p.next
        pre = None
        l2_tail = p  # 第二段（l2） 的开头，但翻转后会变成末尾
        for _ in range(L):
            aft = p.next
            p.next = pre
            pre = p
            p = aft
        dp.next = pre # 接上翻转的列表， 即 1 4 3 2
        l2_tail.next = aft # l2 段 接上剩下没迭代的
        return dummy.next


case1 = ListNode.fromList([3, 5])
ans=Solution().reverseBetween(case1, 1, 2)
print(ans)

# ans = Solution().reverseBetween(ListNode.fromList(list(range(1, 6))), 2, 4)
# print(ans)
