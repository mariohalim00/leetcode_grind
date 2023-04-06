# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Turtle and Hare
        turtle, hare = head, head
        while(hare and hare.next):
            if(hare == turtle): return True
            hare = hare.next.next
            turtle = turtle.next
        
        return False
