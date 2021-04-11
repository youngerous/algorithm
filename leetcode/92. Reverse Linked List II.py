# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return None

        root = ListNode(None)
        start = root
        start.next = head

        # move to reverse-starting index
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # reverse nodes
        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        return root.next