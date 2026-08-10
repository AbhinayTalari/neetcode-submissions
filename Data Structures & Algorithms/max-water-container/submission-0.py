class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, left, right = 0, 0, len(heights) - 1
        while left < right:
            res = max(res, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res