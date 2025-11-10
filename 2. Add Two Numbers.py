# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode(0)
        current_node = out
        while(l1 and l2):
            print(f"current_node: {current_node.val}")
            sum = l1.val + l2.val
            digit = sum % 10
            carry = 1 if sum >= 10 else 0


            #value of current node is current_node.value + digit
            current_node.val = current_node.val + digit
            #if current_node.val already > 0, split it
            if (current_node.val >=10):
                too_big_val = 0
                too_big_val += current_node.val
                digit = too_big_val % 10
                carry = 1
                current_node.val = digit
                next_node = ListNode(carry)
                current_node.next = next_node
                current_node = next_node
           


            #value of next node is carry
                #fist construct next node
                #second set next nodess value to carry          
            next_node = ListNode(carry)
            print(f"sum: {sum} \n digit: {digit} \n carry: {carry} \n curretn_val: {current_node.val} ")


            #set the current_node's next node to next_node
            #then set current_node to have value of next_node
           
           
            '''
            avoid adding trailing 0, like
                l1 = [2,4,3]
                l2 = [5,6,4]
                out = [7,0,8,0]  
            Situation this will happen:
                a. l1.next == None and l2.next == None
                b. carry = 0
            Solution:
                if (not (a and b)):
                    set current_node's next node to be next node
            '''
            if (not (l1.next == None and l2.next == None) ) or carry != 0:
                #"or carry != 0" => prvent [5] + [5] = [0, 1]
                print(f"next_node: {next_node}")
                current_node.next = next_node
                current_node = next_node


            l1 = l1.next
            l2 = l2.next


        #outside while loop -> either l1 or l2 ended early
        remaining_node = None
        if l1:
            remaining_node = l1
        else:
            remaining_node = l2


        while(remaining_node):
            print("in outer while loop")
            sum = current_node.val + remaining_node.val
            digit = sum % 10
            carry = 1 if sum >= 10 else 0
            print(f"digit: {digit} carry: {carry}")


            #value of current node is  digit
            current_node.val = digit


            #short circuit preventing output.last_node.val == 0
            if carry == 0 and remaining_node.next == None:
                print("shorted")
                return out


            #value of next node is carry
                #fist construct next node
                #second set next nodess value to carry          
            next_node = ListNode(carry)


            #set the current_node's next node to next_node
            #then set current_node to have value of next_node
           
            print(f"remaining_node: {remaining_node} remaining_node.next: {remaining_node.next}")
            current_node.next = next_node
            current_node = next_node


            remaining_node = remaining_node.next
     
        return out
       
# Above solutoin really bad.
# Elegant and good solution:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        p = l1
        q = l2
        o = dummy

        while p or q or carry:

            p_val = p.val if p else 0
            q_val = q.val if q else 0

            sum = p_val + q_val + carry

            digit = sum % 10
            carry = sum // 10
            
            o.next = ListNode(digit)
            o = o.next
            if p: p = p.next
            if q: q = q.next
        return dummy.next
