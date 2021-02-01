import itertools


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ix = 0
        senate = list(senate)
        while True:
            if len(senate) == 1:
                break
            for i in itertools.chain(
                    range(ix + 1, len(senate)),
                    range(ix),
            ):
                if senate[i] != senate[ix]:
                    del senate[i]
                    break
            ix += 1
            if ix >= len(senate):
                ix = 0
        return "Dire" if senate[0] == "D" else "Radiant"


print(Solution().predictPartyVictory("DDRRR"))
