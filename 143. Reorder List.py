# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # find middle with slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        rev_head = None
        while slow:
            slow_next = slow.next
            slow.next = rev_head
            rev_head = slow
            slow = slow_next

        # merge both halves
        node = head
        while node:
            node_next = node.next
            node.next = rev_head
            if rev_head:
                rev_head_next = rev_head.next
                rev_head.next = node_next
            node = node_next
            rev_head = rev_head_next