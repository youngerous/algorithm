# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    length = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # leaf node에서는 left, right 각각 0으로 return
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.length = max(self.length, left + right)
            return max(left, right)

        dfs(root)
        return self.length
