#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 is None) and (l2 is None):
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 더 작은 값으로 노드 초기화
        current = ListNode(None)
        result = current
        if l1.val < l2.val:
            current.val = l1.val
            l1 = l1.next
        else:
            current.val = l2.val
            l2 = l2.next

        # 어느 한 쪽이 None이 될 때까지
        while (l1 is not None) and (l2 is not None):
            if current.next is None:
                current.next = ListNode(None)
                current = current.next

            if l1.val < l2.val:
                current.val = l1.val
                l1 = l1.next
            else:
                current.val = l2.val
                l2 = l2.next

        # l1이 None인 경우
        while l2 is not None:
            if current.next is None:
                current.next = ListNode(None)
                current = current.next

            current.val = l2.val
            l2 = l2.next

        # l2가 None인 경우
        while l1 is not None:
            if current.next is None:
                current.next = ListNode(None)
                current = current.next

            current.val = l1.val
            l1 = l1.next

        return result


# @lc code=end
