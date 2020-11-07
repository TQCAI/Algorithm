from typing import List


class Solution:
    def diff(self, s1, s2):
        res = 0
        for a, b in zip(s1, s2):
            if a != b:
                res += 1
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(wordList)
        dist = [[0 for _ in range(N)] for _ in range(N)]
        target_id=None
        begin_ids=[]
        for i,word in enumerate(wordList):
            if word==endWord:
                target_id=i
            if self.diff(beginWord, word)==1:
                begin_ids.append(i)
        if target_id is None or len(begin_ids)==0:
            return 0
        for i in range(1, N):
            for j in range(i):
                dist[i][j] = dist[j][i] = \
                    int(self.diff(wordList[i], wordList[j])==1)

        print(dist)
        return 0


res = Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(res)
