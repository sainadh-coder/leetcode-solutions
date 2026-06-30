# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        curr = l1
        while curr:
            s1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            s2 += str(curr.val)
            curr = curr.next
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        total = str(num1 + num2)
        dummy = ListNode(0)
        curr = dummy
        for digit in total[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next
        