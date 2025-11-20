# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head.next:
            return True
        vals = []
        curr_node = head
        while curr_node.next:
            vals.append(curr_node.val)
            curr_node = curr_node.next
        vals.append(curr_node.val) # don't ignore last element don't 
        print(vals)
        for i in range(0, len(vals)//2):
            j = len(vals)-1 - i
            if vals[i] != vals[j]:
                return False
        return True


