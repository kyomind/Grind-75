# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 使用遞迴解法(適合初學者)
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 設定停止條件
        if root is None:
            return None

        # 交換左右子樹
        root.left, root.right = root.right, root.left

        # 遞迴處理左右子樹
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
