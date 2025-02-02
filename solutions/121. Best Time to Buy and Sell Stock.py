# 暴力法→Time Limit Exceeded
# 時間複雜度：O(n^2)
class Solution1:
    def maxProfit(self, prices):
        max_profit = 0
        for i, p in enumerate(prices):
            # 每一個價格都和後面的價格比較，找出「當次」最大的差值
            # 愈後面比較的範圍愈小
            # 再進行每一輪比較，找出最大的差值
            # 使用 max() 來更新 max_profit 的值，這屬於偷懶的寫法
            max_profit = max(max_profit, max(prices[i:]) - p)
        return max_profit


# 2024-11-29
# 本題只要返回最大利潤，所以不必使用enumerate
class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        # FIXME 這個邊界檢查是多餘的！刪除也不會影響結果
        # 因為 max_profit 預設就是 0，只有一個值時，就會 return 0
        if len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0
        for p in prices:
            # 更新最小買入價，這個比較簡單
            if min_price > p:
                min_price = p

            # XXX 更新「最大利潤」的條件是本題的寫法重點之一
            # 2025-02-02 多一個變數會好讀很多，參考下面寫法
            if p - min_price > max_profit:
                max_profit = p - min_price

        return max_profit


# 2025-02-02
# 簡潔、樸素，但可讀性高，推薦此寫法
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for p in prices:
            if p < min_price:
                min_price = p

            profit = p - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
