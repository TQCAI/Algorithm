from typing import Dict


class Node():
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class DoubleList():
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addLast(self, x: Node):
        x.next = self.tail
        x.prev = self.tail.prev
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DoubleList()
        self.map: Dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key in self.map:
            self.makeRecently(key)
            return self.map[key].v
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.cache.size == self.capacity:
                self.removeLeastRecently()
            self.addRecently(key, value)
        self.removeKey(key)
        self.addRecently(key, value)

    def makeRecently(self, key):
        node = self.map[key]
        self.cache.remove(node)
        self.cache.addLast(node)

    def removeLeastRecently(self):
        first = self.cache.removeFirst()
        self.map.pop(first.k)

    def addRecently(self, key, value):
        node = Node(key, value)
        self.map[key] = node
        self.cache.addLast(node)

    def removeKey(self, key):
        self.cache.remove(self.map.pop(key))
