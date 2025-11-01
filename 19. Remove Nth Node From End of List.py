# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class OnePassSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

class TwoPassSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        index_to_remove = length - n

        prev = None
        curr = head
        curr_index = 0
        while curr:
            if curr_index == index_to_remove:
                if prev == None:
                    head = curr.next
                    return head
                else:
                    prev.next = curr.next
                    curr = curr.next
                    return head
            prev = curr
            curr = curr.next
            curr_index += 1
        return head