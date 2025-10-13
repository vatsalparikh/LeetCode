# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        result = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first_half = head
        second_half = prev
        while second_half:
            result = max(result, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next

        return result

        