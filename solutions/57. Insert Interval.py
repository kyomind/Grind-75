"""
線性掃描，主要有幾步：

一、初始化一個空的結果陣列 new_intervals（題目允許另建一個陣列，不必原地修改）

二、遍歷 intervals 中的每個 interval，分成三種情況處理：
- 若 interval 在 newInterval 的左側（即 interval[1] < newInterval[0]）
    將 interval 加入 new_intervals，因為已經確保不會有重疊
- 若 interval 在 newInterval 的右側（即 interval[0] > newInterval[1]）
    將 newInterval 加入 new_intervals，並將剩餘的區間也全部加入 new_intervals(推薦！)
        因為已經確保不會有重疊
    但也可以更新 newInterval = interval，這樣下一輪就可以處理 新的 interval 直到迴圈結束
        但這樣比較沒有效率，而且難想像
- 若 interval 與 newInterval 有重疊，則更新 newInterval 的範圍，使之包含 interval

三、若遍歷完後 newInterval 尚未加入 new_intervals，將其加入
"""


# 2024-12-09 這個寫法非常簡潔，連len()都沒用到，但可以通過
# 這題基本上就要這樣做，不要管其它了
# XXX 把這解法背(記)下來，比自己慢慢試更有用XD
class Solution1:
    def insert(self, intervals, newInterval):
        new_intervals = []
        for i in intervals:
            if i[1] < newInterval[0]:  # 完全在 newInterval 左側
                new_intervals.append(i)

            elif i[0] > newInterval[1]:  # 完全在 newInterval 右側
                new_intervals.append(newInterval)
                # 2024-12-09 「newInterval = i」這樣寫太抽象了，直接把剩下的加一加會比較直觀
                # 更新 newInterval 直到迴圈結束
                # newInterval = i

                # 新寫法，比較直觀
                new_intervals.extend(intervals[intervals.index(i) :])  # 將剩下的區間加入
                return new_intervals

            else:  # 有重疊，更新 newInterval，但 i 不加入 new_intervals
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])

        new_intervals.append(newInterval)
        return new_intervals


# 更簡單的做法，一旦找到 newInterval 的右側，直接將剩餘的區間全部加入 new_intervals
# - 好吧，我承認，這樣寫並沒有更好懂
# - 反而上面那個更直觀、無腦
# 使用 enumerate 可以得到 index，這樣就可以直接切片加入剩餘的區間
class Solution2:
    def insert(self, intervals, newInterval):
        # 2024-12-09 其實沒必要檢查這個，即使省略也會正常運作
        # 邏輯已經包含在迴圈操作中了
        # 空的話就直接跳過迴圈執行最後兩行，結果相同
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


# 2024-12-09 未完成，這題模式感很強，下次再寫
class Solution:
    def insert(self, intervals, newInterval):
        # 最優先檢查插入點是否可以在兩邊！省得跑迴圈
        # 最左邊
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return
        # 最右邊
        elif newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        new_intervals = []
        for i in intervals:
            # 一一比較或合併，同時還要更新 newInterval
            pass
