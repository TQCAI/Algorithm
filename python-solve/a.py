class Solution:
    def permutation(self, s: str) -> List[str]:
        path = list(s)
        ans = []
        L = len(path)

        def backtrace(t):
            if t == L - 1:  #
                ans.append("".join(path))
                return
            for i in range(t, L):  #
                path[t], path[i] = path[i], path[t]
                backtrace(t + 1)
                path[t], path[i] = path[i], path[t]

        backtrace(0)
        return list(set(ans))
