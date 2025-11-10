# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0)
        while(l1 and l2):
            sum = l1.val + l2.val
            digit = int(sum % 10)
            carry = int((sum - digit)/10)

            out.val = digit + out.val
            out_next = ListNode(carry)
            out.next = out_next
            print(out)
            out = out_next

            l1 = l1.next
            l2 = l2.next
            # print(f"sum: {sum} digit: {digit} carry: {carry}")
        
        # print(out)

            


