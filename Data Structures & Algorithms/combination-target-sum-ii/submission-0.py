class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                cur.append(candidates[j])
                backtrack(j + 1, cur, total + candidates[j])
                cur.pop()
        backtrack(0, [], 0)
        return res