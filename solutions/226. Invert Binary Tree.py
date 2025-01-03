# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 使用遞迴解法(適合初學者)
class Solution1:
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 設定停止條件
        # 2024-11-30 遇到葉節點或root是空的時有效
        if root is None:
            return None

        # 交換左右子樹
        root.left, root.right = root.right, root.left

        # 遞迴處理左右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 2024-11-30 遞迴 + 後序遍歷
class Solution:
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        root.right, root.left = root.left, root.right
        # 先左或右都可以
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
