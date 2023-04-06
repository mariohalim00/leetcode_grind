# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None): return None
        newHead = head
        if(head.next):
           newHead = self.reverseList(head.next)
           print(self.reverseList(head.next))
           head.next.next = head
        head.next = None
        return newHead

        # # ITERATIVE
        # prevNode = None
        # curr = head
        # while(curr != None):
        #     nextNode = curr.next
        #     curr.next = prevNode
        #     prevNode = curr
        #     curr = nextNode

        # head = prevNode
        
        # return head

