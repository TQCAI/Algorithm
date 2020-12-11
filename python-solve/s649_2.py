import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_list = collections.deque()
        d_list = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                r_list.append(i)
            else:
                d_list.append(i)

        while r_list and d_list:
            if r_list[0] < d_list[0]:
                r_list.append(r_list[0] + n)
            else:
                d_list.append(d_list[0] + n)
            r_list.popleft()
            d_list.popleft()

        return "Radiant" if r_list else "Dire"

print(Solution().predictPartyVictory("RD"))
