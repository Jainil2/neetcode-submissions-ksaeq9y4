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
        if not head:
            return None
        freq = {}
        dummy = head
        while dummy:
            freq[dummy] = Node(dummy.val)
            dummy = dummy.next
        dummy = head
        while dummy:
            if dummy.next:
                freq[dummy].next = freq[dummy.next]
            if dummy.random:
                freq[dummy].random = freq[dummy.random]
            dummy = dummy.next
        return freq[head]