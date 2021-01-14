from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        vis = set()
        origin = "0000"
        queue.append(origin)
        # vis.add(origin)
        invalid_set = set(deadends)
        if origin in invalid_set:
            return -1

        def modify(state, i, delta):
            c = state[i]
            c = str((int(c) + delta) % 10)
            return state[:i] + c + state[i + 1:]

        cnt = 0
        while queue:
            sz = len(queue)
            while sz:
                state = queue.pop(0)
                if state in invalid_set:
                    continue
                vis.add(state)
                if state == target:
                    return cnt
                for delta in (-1, 1):
                    for i in range(4):
                        sub_state = modify(state, i, delta)
                        queue.append(sub_state)
                sz -= 1
            cnt += 1
        return -1


res = Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
print(res)
