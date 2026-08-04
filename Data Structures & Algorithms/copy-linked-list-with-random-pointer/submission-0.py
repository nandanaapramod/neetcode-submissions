"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        toCopy={None: None}

        cur=head
        
        while cur:
            copy=Node(cur.val)
            toCopy[cur]=copy
            cur=cur.next
        cur=head

        while  cur:
            copy=toCopy[cur]
            copy.next=toCopy[cur.next]
            copy.random=toCopy[cur.random]
            cur=cur.next
        return toCopy[head]