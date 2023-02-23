class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_vol = 0
        while l < r:
            min_height = min(height[l], height[r])
            length = r - l
            tmp_vol = min_height * length
            max_vol = max(max_vol, tmp_vol)

            if(height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        return max_vol
