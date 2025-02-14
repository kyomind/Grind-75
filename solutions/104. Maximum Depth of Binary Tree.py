# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 這基本上就是標準的 DFS，後序遍歷，可以說要牢記於心
class Solution1:
    def maxDepth(self, root):
        # 一定要有停止條件 2024-12-08
        if not root:
            return 0

        # 不是空節點就直接遞迴計算左右節點高度
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # 這個是關鍵，最後回傳並增加高度
        return max(left, right) + 1 # 當前節點的高度


class Solution:
    # 注意，它本身就要設計成遞迴函式
    def maxDepth(self, root):
        """其實起始值就是終止條件的0
        過程中的遞加靠另一個return的+1實現
        所以中間不需要額外的max_depth這種初始化了
        """
        # 終止條件
        # if root.val is None: XXX 錯誤，是root「本身」是None，而不是值
        if root is None:
            return 0

        max_depth = 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 每一次都要更新 max_depth，而且要 return
        # 不需要寫這麼麻煩啦！ XXX
        max_depth = max(max_depth, max(left_depth, right_depth) + 1)
        return max_depth
