class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next  # Save next node
            curr.next = prev  # Reverse link
            prev = curr       # Move prev and curr
            curr = temp
        return prev           # New head
        