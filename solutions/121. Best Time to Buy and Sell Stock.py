# 暴力法→Time Limit Exceeded
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i, p in enumerate(prices):
            # 每一個價格都和後面的價格比較，找出「當次」最大的差值
            # 愈後面比較的範圍愈小
            # 再進行每一輪比較，找出最大的差值
            # 使用 max() 來更新 max_profit 的值，這屬於偷懶的寫法
            max_profit = max(max_profit, max(prices[i:]) - p)
        return max_profit


# 不要用max()，而是用if來更新max_profit
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0  # 初始化最大利潤
        for i in range(len(prices)):  # 外層迴圈遍歷每個買入日
            max_price = prices[i]  # 初始化 max_price 為當前價格
            # 手動遍歷後續的價格，找出最大賣出價格
            for j in range(i + 1, len(prices)):
                if prices[j] > max_price:
                    max_price = prices[j]
            # 更新最大利潤，不使用 max 函式
            potential_profit = max_price - prices[i]
            if potential_profit > max_profit:
                max_profit = potential_profit
        return max_profit


# 單次遍歷法
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 0
        max_profit = 0
        for i, p in enumerate(prices):
            # 初始化最小價格為第一天的價格
            if i == 0:
                min_price = p
                continue

            """以下兩件事情不會同時發生：(所以用 if/else 或 if/elif 都可以，只是後者更直觀)
            - 如果當前價格是新的最小價格，則更新 min_price。
            - 如果當前價格減去最小價格的利潤比目前的最大利潤還大，則更新 max_profit。
            注意：當 min_price 被更新時，當前 p 無法帶來利潤，因此 max_profit 不會更新。"""

            # 如果當前價格比最小價格還小，就更新最小價格
            if p < min_price:
                min_price = p
            # 如果當前價格減去最小價格大於最大利潤，就更新最大利潤
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit
