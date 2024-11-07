"""
線性掃描，主要有幾步：

一、初始化一個空的結果陣列 new_intervals（題目允許另建一個陣列，不必原地修改）

二、遍歷 intervals 中的每個 interval，分成三種情況處理：
- 若 interval 在 newInterval 的左側（即 interval[1] < newInterval[0]），將 interval 加入 new_intervals
    因為已經確保不會有重疊
- 若 interval 在 newInterval 的右側（即 interval[0] > newInterval[1]）
    將 newInterval 加入 new_intervals，並將剩餘的區間也全部加入 new_intervals，因為已經確保不會有重疊
    但也可以更新 newInterval = interval，這樣下一輪就可以處理 interval，直到迴圈結束(比較沒有效率)
- 若 interval 與 newInterval 有重疊，則更新 newInterval 的範圍，使之包含 interval

三、若遍歷完後 newInterval 尚未加入 new_intervals，將其加入
"""


class Solution1(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_intervals = []
        for i in intervals:
            if i[1] < newInterval[0]:  # 完全在 newInterval 左側
                new_intervals.append(i)

            elif i[0] > newInterval[1]:  # 完全在 newInterval 右側
                new_intervals.append(newInterval)
                # 更新 newInterval 直到迴圈結束
                newInterval = i

            else:  # 有重疊，更新 newInterval，但 i 不加入 new_intervals
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        new_intervals.append(newInterval)
        return new_intervals


# 更簡單的做法，一旦找到 newInterval 的右側，直接將剩餘的區間全部加入 new_intervals
# - 好吧，我承認，這樣寫並沒有更好懂
# - 反而上面那個更直觀、無腦
# 使用 enumerate 可以得到 index，這樣就可以直接切片加入剩餘的區間
class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        new_intervals = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                new_intervals.append(interval)
            elif interval[0] > newInterval[1]:
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[i:])
                return new_intervals
                # 也可以寫成下面這樣
                # 注意 [newInterval] 是一個 list，這樣才能相加
                # return new_intervals + [newInterval] + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # 這兩行是必要的，因為可能 newInterval 在 intervals 的最後一個區間的右側
        # XXX 這個方法仍然無法省略這兩行，我感覺也不是很好
        new_intervals.append(newInterval)
        return new_intervals
