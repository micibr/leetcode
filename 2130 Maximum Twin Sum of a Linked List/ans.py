# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):

        val = []
        ans = []

        curr = head
        while curr:
            val.append(curr.val)
            curr = curr.next

        i = 0
        while i <= (len(val) // 2) - 1:
            ans.append(val[len(val) - 1 - i] + val[i])
            i += 1

        return max(ans)

