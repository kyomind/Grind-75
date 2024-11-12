# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 使用 BFS 進行層序遍歷 + queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        # 初始化佇列，將根節點加入佇列
        # XXX 這裡使用 list 來模擬 queue，在移除第一個元素時，效率較低
        # 實際上可以使用 collections.deque 來實現，移除時則使用 popleft() 方法
        queue = [root]

        # 開始 BFS
        while queue:
            # 初始化當前層級的結果集
            current_level = []
            # 獲取當前隊列的長度
            level_length = len(queue)

            # 遍歷當前層級的所有節點
            for _ in range(level_length):
                # 將隊列中的節點取出
                node = queue.pop(0)
                current_level.append(node.val)  # 到這裡為止，已經完成了一層的遍歷

                # XXX 第二部分：從 queue 中的節點加入其子節點，以便進行下一層的遍歷
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(current_level)

        return levels


# 使用 DFS 進行層序遍歷 + 遞迴
# FIXME 尚未深入理解
class Solution1:
    def levelOrder(self, root: TreeNode) -> list:
        levels = []
        if not root:
            return levels

        def traverse_tree_by_level(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                traverse_tree_by_level(node.left, level + 1)
            if node.right:
                traverse_tree_by_level(node.right, level + 1)

        traverse_tree_by_level(root, 0)
        return levels
