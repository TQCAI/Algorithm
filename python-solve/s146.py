from typing import Optional, Dict


class Node:
    def __init__(self, k, v):
        self.v = v
        self.k = k
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoubleList:
    '''意我们实现的双链表 API 只能从尾部插入，也就是说靠尾部的数据是最近使用的，靠头部的数据是最久为使用的。'''

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, x: Node):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first: Node = self.head.next
        self.remove(first)
        return first


class LRUCache:

    def __init__(self, capacity: int):
        '''将某个 key 提升为最近使用的'''
        self.capacity = capacity
        self.map: Dict[int, Node] = {}
        self.cache = DoubleList()

    def makeRecently(self, key):
        '''添加最近使用的元素'''
        x: Node = self.map[key]
        self.cache.remove(x)
        self.cache.addLast(x)

    def addRecently(self, key: int, val: int):
        x = Node(key, val)
        self.cache.addLast(x)
        self.map[key] = x

    def deleteKey(self, key):
        x: Node = self.map[key]
        self.cache.remove(x)
        self.map.pop(key)

    def removeLeastRecently(self):
        deletedNode = self.cache.removeFirst()
        self.map.pop(deletedNode.k)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.makeRecently(key)
        return self.map[key].v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # 删除旧的数据
            self.deleteKey(key)
            # 新插入的数据为最近使用的数据
            self.addRecently(key, value)
            return
        if self.capacity == self.cache.size:
            # 删除最久未使用的元素
            self.removeLeastRecently()
        # 添加为最近使用的元素
        self.addRecently(key, value)


ops = ["LRUCache", "put", "put", "get", "put", "put", "get"]
data = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
lru = LRUCache(data[0][0])
for op, datum in zip(ops[1:], data[1:]):
    print(op, datum)
    func = getattr(lru, op)
    ans = func(*datum)
    print(ans)
