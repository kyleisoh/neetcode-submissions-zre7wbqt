# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr, curr2 = l1, l2
        sumNode = ListNode(0, None)
        head = sumNode

        carry = 0
        while curr or curr2 or carry:
            v1 = curr.val if curr else 0
            v2 = curr2.val if curr2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            sumNode.next = ListNode(val)

            # Update ptrs
            sumNode = sumNode.next
            curr = curr.next if curr else None
            curr2 = curr2.next if curr2 else None
        
        return head.next
