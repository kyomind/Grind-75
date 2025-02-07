# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2024-11-30 遞迴
class Solution2:
    def invertTree(self, root):
        if root is None:
            return None

        root.right, root.left = root.left, root.right
        # 先左或右都可以
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root


# 2025-02-07
# XXX 重點是：先處理當前節點，再處理左右子節點，邏輯都一樣，所以使用遞迴
# 這算是一種「前序遍歷」
class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        # 先翻轉(處理)右左子樹, 這是處理 XXX 「當前節點」
        # root.left = root.right XXX 這樣寫是不行的！只能寫在一行，不然就要「中間變數」來交換
        # root.right = root.left
        root.left, root.right = root.right, root.left

        # 遞迴處理 XXX 「子節點」的左右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
