# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        slow.next = None

        list1 = head
        list2 = tmp

        # reverse list 2 
        prev = None
        curr = list2
        while(curr):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        list2 = prev

        while(list2):
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1 = tmp1
            list2 = tmp2
            
        # print(head)
