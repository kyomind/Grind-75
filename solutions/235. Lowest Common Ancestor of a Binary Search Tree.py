# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
初步思考
- 既然是二元搜尋樹，那這一定有意義，中序遍歷是有序的升冪序列
- 結果一定是 p <= result <= q 或 q <= result <= p（因為 q、p 沒有固定誰大誰小）
- 二元搜尋樹，中序遍歷是有序的，所以我們可以利用這個特性，這是 DFS 的一種，要使用遞迴
- 根節點與左右子樹的固定關係，可以用來遞迴判斷，結果一定在哪裡——這是重點
"""


# 遞迴法
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 如果 p、q 都比 root 小，那麼結果一定在左子樹(而不是當前的 root)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 如果 p、q 都比 root 大，那麼結果一定在右子樹(而不是當前的 root)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # 停止條件
        else:
            # 這個 else 包括了兩種情況:
            # - p 和 q 分佈在 root 的兩側
            # - root 是 p 或 q，並且另一個節點位於 root 的一側
            return root


"""
方法觀察
- 不需要比對很深，只要比對到 p、q 一大一小的情況就可以停止，即使 p、q 離 root 很遠
- 這個命題的最關鍵是：二元搜尋樹的特性，左子樹的「所有節點」都比 root 小，右子樹的所有節點都比 root 大
- 只要 p、q 一大一小於 root，那麼 root 就是我們要的結果！
- ps 這裡的一大一小，指的都是排除兩者皆大於 root 或皆小於 root 的情況
"""


# 迭代法
# 效能上比遞迴法好，因為不需要遞迴的 stack 開銷
def lowestCommonAncestor(root, p, q):
    # 無限迴圈，直到找到答案才 return
    # - 目標是找到符合條件的 root
    # 所以寫 while True 也行
    while root:
        if p.val < root.val and q.val < root.val:
            # 向樹的下一層移動，這裡是左子樹
            root = root.left
        elif p.val > root.val and q.val > root.val:
            # 向樹的下一層移動，這裡是右子樹
            root = root.right
        # 停止條件，找到答案
        else:
            return root
