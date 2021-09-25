# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode()
        l3_copy = l3
    
        carry = 0
        
        while True:
            sum = l1.val + l2.val
            
            if sum+carry < 10 :
                l3.val = sum + carry
                carry = 0
                if l1.next == None and l2.next == None:
                    break
                else:
                    l3.next = ListNode(0)
                    l3 = l3.next
            
            else:
                l3.val = (sum+carry)%10
                carry = 1
                if l1.next == None and l2.next == None:
                    l3.next = ListNode(carry)
                    break
                else:
                    l3.next = ListNode(0)
                    l3 = l3.next
            
            l1 = l1.next
            l2 = l2.next

            if l1==None and l2!=None:
                l1 = ListNode()
                l1.val = 0

            if l1!=None and l2==None:
                l2 = ListNode()
                l2.val = 0

        return l3_copy