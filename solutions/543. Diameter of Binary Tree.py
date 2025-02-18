# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 這題和 110. Balanced Binary Tree 類似
# 所以都需要一個 helper function，來計算每個節點的高度
# 節點的高度，即當前節點到最遠葉節點的距離
class Solution0:
    def diameterOfBinaryTree(self, root):
        # 全部變數都放在這裡，這樣才能在遞迴中更新
        self.diameter = 0

        # DFS，使用遞迴，使用後序遍歷，因為只有後序遍歷，才會優先計算左右子樹的高度
        def check_height(node):
            if not node:
                return 0

            # 遞迴計算左右子樹的高度
            left = check_height(node.left)
            right = check_height(node.right)

            # 更新最大直徑，這和計算高度沒有直接關係
            # 只是在過程中一併更新最大直徑
            self.diameter = max(self.diameter, left + right)

            # +1 是因為自下而上，每個節點的高度都要加1
            return max(left, right) + 1

        check_height(root)
        return self.diameter


# ChatGPT 版本(大同小異，主要是參考註解)
class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 2024-12-08 其實樹的直徑本來就有「最大」的意思，所以這命名有點不精確
        self.max_diameter = 0  # 用來儲存全域最大的直徑

        def dfs(node):
            if not node:
                return 0  # 空節點的高度為 0

            # 計算左子樹和右子樹的高度
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # 更新直徑（左子樹高度 + 右子樹高度）
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # 返回當前節點的高度：1 + max(左子樹高度, 右子樹高度)
            return 1 + max(left_height, right_height)

        dfs(root)  # 從根節點開始進行深度優先搜索
        return self.max_diameter


# 2024-12-08
class Solution:
    def diameterOfBinaryTree(self, root):
        # 這裡只要記得self所擁有的屬性，在方法內是全域
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            # 和110題一樣，節點不是none，就直接開始計算了！
            right_height = dfs(node.right)
            left_height = dfs(node.left)

            # XXX 唯一的不同就是在過程中更新直徑
            total_height = right_height + left_height
            if total_height > self.diameter:
                self.diameter = total_height

            # XXX 一定有一個地方，是會讓這個高度值增加的
            # 每一層遞迴高度只會加1而已，就在return
            return max(right_height, left_height) + 1

        # 記得要呼叫啊！不然定義了也沒用
        dfs(root)

        return self.diameter


