# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse linked list
        reversed_l1 = self.reverse_linked_list(l1)
        reversed_l2 = self.reverse_linked_list(l2)

        # convert linked list into list
        list_l1 = self.to_list(reversed_l1)
        list_l2 = self.to_list(reversed_l2)

        # concat list elements and convert into integer
        final_l1 = int("".join(map(str, list_l1)))
        final_l2 = int("".join(map(str, list_l2)))

        # return reversed linked list
        return self.to_reversed_linked_list(str(final_l1 + final_l2))

    def reverse_linked_list(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def to_list(self, node: ListNode) -> list:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def to_reversed_linked_list(self, elements: str) -> ListNode:
        prev = None
        for elem in elements:
            node = ListNode(elem)
            node.next = prev
            prev = node
        return node


class Solution2:
    """
    전가산기(Full Adder)의 원리를 활용한 풀이
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            total = 0
            # 두 입력값의 합 계산
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            # 몫(자리올림수)와 나머지(값) 계산
            carry, val = divmod(total + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
