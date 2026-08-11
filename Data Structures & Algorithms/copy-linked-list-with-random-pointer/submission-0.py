class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}
        cur = head
        # Create copies in map
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        # Set next and random pointers
        while cur:
            oldToCopy[cur].next = oldToCopy.get(cur.next)
            oldToCopy[cur].random = oldToCopy.get(cur.random)
            cur = cur.next

        return oldToCopy.get(head)