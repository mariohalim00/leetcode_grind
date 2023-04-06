# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None and list2 == None):
            return list1
        if(list1 == None and list2 != None):
            return list2
        if(list2 == None and list1 != None):
            return list1
        
        dummy = ListNode()
        
        curr1 = list1
        curr2 = list2
        curr3 = dummy
        while(curr1 and curr2):
            if(curr1.val <= curr2.val):
                nextNode = curr1.next
                curr1.next = None
                curr3.next = curr1
                curr1 = nextNode
            else:
                nextNode = curr2.next
                curr2.next = None
                curr3.next = curr2
                curr2 = nextNode
            curr3 = curr3.next
        
        if curr1:
            curr3.next = curr1
        elif curr2:
            curr3.next = curr2
        return dummy.next


        