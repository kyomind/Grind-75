import heapq

# 兩種做法：使用 heapq 或是 quick select


# 這裡先用 heapq
# 1. 先將所有點的距離計算出來，並且存到 heap 中
# 2. 依序取出 heap 中的前 k 個元素，即為答案
# 使用 max heap，因為我們要取出最小的 k 個元素，所以要將距離取負號
class Solution(object):
    def kClosest(self, points, k):
        """
        找出 k 個最接近原點(0,0)的點
        :param points: 點的列表，每個點為 [x,y] 座標
        :param k: 要返回的最近點的數量
        :return: k 個最近的點的列表
        """
        max_heap = []  # 用來儲存點的最大堆積(max heap)

        for x, y in points:
            # 計算每個點到原點的距離的平方和(不需要開根號)
            # 取負號是因為 heapq 預設是最小堆積(min heap)
            # 我們需要保留最小的 k 個距離，所以用負號轉換成最大堆積
            dist = -(x * x + y * y)

            if len(max_heap) == k:
                # 如果堆積已經有 k 個元素——堆積已滿
                # heappushpop 會先加入新元素，再彈出最小值
                # 這樣就能保持堆積中始終有 k 個距離最小的點
                # XXX dist 是負數，所以最小值實際上是最大值
                # XXX dist 之所以要放在第一個位置，是因為 heapq 會以第一個元素排序
                heapq.heappushpop(max_heap, (dist, x, y))
            else:
                # 堆積還沒滿，直接加入新元素
                heapq.heappush(max_heap, (dist, x, y))

        # 不需要距離資訊，所以只取 x, y
        return [(x, y) for (_, x, y) in max_heap]
