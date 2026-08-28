class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            r1, r2 = 0, 0
            for n in arr:
                r1, r2 = r2, max(r2, r1 + n)
            return r2

        return max(helper(nums[1:]), helper(nums[:-1]))