class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if(i >= len(nums)):
                res.append(subset.copy())
                return

            # CASE INCLUDE NUMS[I]
            subset.append(nums[i])
            dfs(i + 1)

            # CASE NOT INCLUDE NUMS[I]
            subset.pop()
            dfs(i + 1)
    
        dfs(0)
        return res
            