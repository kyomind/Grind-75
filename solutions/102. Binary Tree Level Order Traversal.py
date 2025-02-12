# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 使用 BFS 進行層序遍歷 + queue
# 這過程和爬蟲一個網站非常像
class Solution2:
    def levelOrder(self, root):
        levels = []
        if not root:
            return levels

        # 初始化佇列，將根節點加入佇列
        # XXX 這裡使用 list 來模擬 queue，在移除第一個元素時，效率較低
        # 可以使用 collections.deque 來實現，移除時則使用 popleft() 方法
        # queue = deque([root])
        queue = [root]

        # 開始 BFS
        while queue:
            # 初始化當前層級的結果集
            current_level = []
            # 獲取當前佇列的長度
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


# 2024-12-14
class Solution3:
    def levelOrder(self, root):
        # 空節點
        if root is None:
            return []

        levels = []
        queue = [root]

        while queue:
            # 佇列在每一層會重新收集元素
            # 只要該層有元素，while就會成立，反之不成立
            # 元素的收集只在兩個地方
            # 1. 初始化時，即 queue = [root]
            # 2. 每一層遍歷時，即下面的 for 迴圈的後半部
            nodes_of_current_level = []  # 結果收集器
            level_length = len(queue)
            for _ in range(level_length):
                # node = queue.pop(index=0) 不可以用關鍵字引數！噗
                node = queue.pop(0)
                nodes_of_current_level.append(node.val)

                # XXX 這裡是重點，取出一個node與值的同時，同時也要存下它的子節點供下一層使用
                # 最多也只有兩個子節點而已
                # 這裡就是queue補充待訪節點的地方！也就是上述的「2.」
                # XXX 注意，有順序！先左再右！！！
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(nodes_of_current_level)

        return levels


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        levels = []
        queue = [root]
        while queue:
            level_vals = []
            level_length = len(queue)
            # for i in queue:
            # XXX 我知道為不能直接for這個queue了，因為中間要"修改"它，所以不能同時操作
            # 但用index就可以，相當於queue的「替身」
            # 因此「長度」是必要的，這是替身們的分界

            # 也可以直接寫成 `for _ in range(len(queue)):`，省略變數level_length
            for _ in range(level_length):
                # node = queue[-1] XXX 要pop才行，不然queue永遠不會減少只會增加
                node = queue.pop(0)
                level_vals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level_vals)

        return levels
