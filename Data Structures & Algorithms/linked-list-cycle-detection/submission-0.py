class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # 1 step
            fast = fast.next.next  # 2 steps
            if slow == fast:
                return True
        return False