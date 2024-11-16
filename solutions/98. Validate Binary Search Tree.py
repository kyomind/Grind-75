# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float("-inf")

        def is_valid_in_order(node):
            if not node:
                return True

            # 優先遞迴遍歷左子樹，因為是中序遍歷
            if not is_valid_in_order(node.left):
                return False

            # 嚴格遞增條件檢查，必須是「大於」當前節點值
            if node.val <= self.prev:
                return False

            # 更新 self.prev 為當前節點值
            self.prev = node.val

            # 遞迴遍歷右子樹
            return is_valid_in_order(node.right)

        # 開始中序遍歷
        return is_valid_in_order(root)
