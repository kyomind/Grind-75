# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
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


# 2024-12-03
# 這次按照文件說的，helper函式回傳兩個值：是否平衡、高度
# FIXME
class Solution2:
    def isBalanced(self, root):
        # 遞迴、後序遍歷(先處理兩個子樹)
        # return is_balanced, height
        def helper(root):
            # 停止條件: 先處理空節點或葉節點的子節點(空)
            if root is None:
                return True, 0

            # 處理左右節點比較
            # 有右節點(左右順序都可)
            # FIXME 錯誤，因為當節點不為空時，就要「直接比較」子節點是否平衡了！
            if root.left:
                return helper(root.left)


class Solution:
    def isBalanced(self, root):
        def helper(root):
            # 停止條件: 先處理空節點或葉節點的子節點(空)
            if root is None:
                return True, 0

            # 節點不為空，比較左右節點！
            is_balanced_left, height_left = helper(root.left)
            if not is_balanced_left:
                return False, -1

            is_balanced_right, height_right = helper(root.right)
            if not is_balanced_right:
                return False, -1

            # 確定兩邊「子樹」都是平衡，繼續比較當前節點
            if abs(height_right - height_left) > 1:
                return False, -1

            return True, max(height_left, height_right) + 1

        return helper(root)[0]
