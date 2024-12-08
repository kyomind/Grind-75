# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 這基本上就是標準的 DFS，後序遍歷，可以說要牢記於心
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 這個是關鍵 2024-12-08
        return max(left, right) + 1
