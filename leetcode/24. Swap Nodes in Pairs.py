# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(None)
        prev.next = head
        root = prev

        while head and head.next:
            # 인접한 두 노드의 위치 변경
            b = head.next
            head.next = head.next.next
            b.next = head

            # 위치가 변경된 상태에서 다음 노드 가리킴
            prev.next = b

            # 다음 쌍의 노드로 이동
            head = head.next
            prev = prev.next.next

        return root.next
