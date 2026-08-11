from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output, q = [], deque()
        for i, num in enumerate(nums):
            # Remove indices out of window
            if q and q[0] < i - k + 1:
                q.popleft()
            # Remove smaller elements
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            # Add max to output
            if i >= k - 1:
                output.append(nums[q[0]])
        return output