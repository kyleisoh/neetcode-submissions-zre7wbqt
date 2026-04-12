# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumNode = ListNode(0, None)
        curr, curr2 = l1, l2
        head = sumNode
        carry = 0

        while curr is not None and curr2 is not None:
            sumDigit = curr.val + curr2.val + carry
            if sumDigit > 9:
                carry = 1
                sumDigit -= 10
            else:
                carry = 0
            
            sumNode.val = sumDigit
            if curr.next or curr2.next:
                sumNode.next = ListNode(0, None)
                sumNode = sumNode.next
            curr, curr2 = curr.next, curr2.next

        if curr:
            while curr is not None:
                sumDigit = curr.val + carry
                if sumDigit > 9:
                    carry = 1
                    sumDigit -= 10
                else:
                    carry = 0

                sumNode.val = sumDigit
                if curr.next:
                    sumNode.next = ListNode(0, None)
                    sumNode = sumNode.next
                curr = curr.next
        
        elif curr2:
            while curr2 is not None:
                sumDigit = curr2.val + carry
                if sumDigit > 9:
                    carry = 1
                    sumDigit -= 10
                else:
                    carry = 0

                sumNode.val = sumDigit
                if curr2.next:
                    sumNode.next = ListNode(0, None)
                    sumNode = sumNode.next
                curr2 = curr2.next
        
        if not curr and not curr2 and carry:
            sumNode.next = ListNode(carry, None)

        return head
        

        