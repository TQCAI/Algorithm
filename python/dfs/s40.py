from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def dfs(begin, target, path):
            if target == 0:
                ans.append(path)
                return
            for i in range(begin, n):
                if target - candidates[i] < 0:
                    break
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, target - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return ans


ans = Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
print(ans)
