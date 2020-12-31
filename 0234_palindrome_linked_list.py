from collections import deque
from helper import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        nodes = deque()
        while head:
            nodes.append(head.val)
            head = head.next
        
        while len(nodes) > 1:
            if nodes.popleft() != nodes.pop():
                return False
        return True       
   