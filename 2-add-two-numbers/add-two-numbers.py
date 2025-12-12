# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def fn(l1, l2, carry):

            if not l1 and not l2:
                if carry != 0:
                    new = ListNode(carry)
                    return new
                else:
                    return None

            if not l1:
                summ = l2.val + carry
                carry = summ // 10
                num = summ % 10
                new = ListNode(num)
                new.next = fn(None, l2.next, carry)
                return new

            if not l2:
                summ = l1.val + carry
                carry = summ // 10
                num = summ % 10
                new = ListNode(num)
                new.next = fn(l1.next, None, carry)
                return new

            summ = l1.val + l2.val + carry
            carry = summ // 10
            num = summ % 10
            new = ListNode(num)
            new.next = fn(l1.next, l2.next, carry)
            return new

        return fn(l1, l2, 0)