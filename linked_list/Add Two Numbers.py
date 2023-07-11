##### Check out the if else technique this is good example of thinking before coding




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        temp = head
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = (val1+val2 + carry)%10
            carry = (val1+val2+ carry)//10
            temp.next = ListNode(val)
            temp = temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry!=0:
            temp.next = ListNode(carry)
            
        return head.next





        
            

        
