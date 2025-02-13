# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isValidBST(self, root: TreeNode | None) -> bool:
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


# 2025-02-13 先用上面寫法，之前再考慮用範例寫法
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.prev = float("-inf")

        def validate(node):
            """注意：所有的判斷、檢查基本上都要return
            而且遞迴函式都要return
            """
            if not node:
                return True

            # 嚴格用中序遍歷順序：左子樹、當前節點、右子樹

            # 左子樹
            # if validate(node.left): 錯誤寫法，因為true要繼續，所以應該要驗false
            if not validate(node.left):
                return False
            # 當前節點
            if not node.val > self.prev:
                return False

            self.prev = node.val

            # 右子樹
            # if not validate() ... 錯誤，要 return
            # 相當於以下寫法，但顯然這樣寫更簡潔而已
            # if not validate(node.right):
            #    return False
            # return True ——全部都檢查了都正確時
            return validate(node.right)

        return validate(root)
