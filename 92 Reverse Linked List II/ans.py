from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(next=head)
        #move to left
        curr, prev = head, dummy
        i = 1
        while i < left:
            prev = curr
            curr = curr.next
            i += 1

        before_reverse = prev
        start = curr
        prev = None
        
        #reverse linked list
        while i <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        #reattatch 
        before_reverse.next = prev
        start.next = curr

        return dummy.next

            
            

