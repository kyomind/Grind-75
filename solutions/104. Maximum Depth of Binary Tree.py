# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 這基本上就是標準的 DFS，後序遍歷，可以說要牢記於心
# + 2024-12-08
class Solution:
    def maxDepth(self, root):
        # 一定要有停止條件 2024-12-08
        if not root:
            return 0

        # 不是空節點就直接遞迴計算左右節點高度
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 這個是關鍵，最後回傳並增加高度
        return max(left, right) + 1
