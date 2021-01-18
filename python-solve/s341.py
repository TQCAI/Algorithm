from typing import List


class NestedInteger:
    val = 0


def isInteger(self) -> bool:
    """
    @return True if this NestedInteger holds a single integer, rather than a nested list.
    """
    return isinstance(self.val, int)


def getInteger(self) -> int:
    """
    @return the single integer that this NestedInteger holds, if it holds a single integer
    Return None if this NestedInteger holds a nested list
    """
    return self.val


def getList(self) -> [NestedInteger]:
    return [self.val]


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.nestedList = list(nestedList)

    def next(self) -> int:
        return self.nestedList.pop(0).getInteger()


    def hasNext(self) -> bool:
        while self.nestedList and (not self.nestedList[0].isInteger()):
            first = self.nestedList.pop(0).getList()
            for item in reversed(first):
                self.nestedList.insert(0, item)
        return self.nestedList


niter = NestedIterator([NestedIterator([1, 1]), 2, NestedIterator([1, 1])])
niter = NestedIterator([[1, 1, [[[2]]]], 2, [1, 1]])
for i in range(6):
    print(niter.next())
