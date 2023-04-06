# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # old way
        # get length o(n)
        # subtract length to n to delete the Mth from start
        # move to target, while keeping prev node and then delete O(m)
        # approx O(n + m)

        # new way use sliding window/ two pointer approach
        #init dummy to make things easier
        dummy = ListNode(0, head)
        left, right = dummy, dummy
        while(n > 0):
            right = right.next
            n -= 1

        while( right.next != None ):
            left = left.next
            right = right.next

        left.next = left.next.next
        head = dummy.next

        return head
