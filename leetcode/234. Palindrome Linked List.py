# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        numbers = []
        node = head
        while node is not None:
            numbers.append(node.val)
            node = node.next

        return numbers == numbers[::-1]
