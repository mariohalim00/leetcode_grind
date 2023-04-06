class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, sum_arr, total):
            if(idx >= len(candidates)): return
            if(total > target): return
            if(total == target):
                res.append(sum_arr.copy())
                return 

            sum_arr.append(candidates[idx])
            dfs(idx, sum_arr, total + candidates[idx])

            sum_arr.pop()
            dfs(idx + 1, sum_arr, total)

        dfs(0, [], 0)
        return res
