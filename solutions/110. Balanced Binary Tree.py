# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def check_height(node):
            # 空節點的高度為0
            if not node:
                return 0

            # 確認左右子樹高度，如果左右子樹的高度差超過1，表示不是平衡二元樹，則回傳-1，結束遞迴
            # 如果左右子樹的高度差沒有超過1，則回傳高度
            # XXX 注意：這裡的-1是一個flag，表示不是平衡二元樹，正常的時候則是回傳高度

            # 先確認左子樹
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            # 再確認右子樹
            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            # 如果左右子樹的高度差超過1，則回傳-1
            # 此時已確定不是平衡二元樹
            if abs(left_height - right_height) > 1:
                return -1

            # 已確定是平衡二元樹，回傳高度
            # 高度為左右子樹的最大高度+1(加上根節點自己的高度)
            return max(left_height, right_height) + 1

        return check_height(root) != -1
