# by ChatGPT
class Solution:
    def climbStairs(self, n: int) -> int:
        # 如果樓梯數只有 1 階，直接返回 1
        if n == 1:
            return 1

        # 初始化 dp 陣列，大小為 n+1（包含第 0 階和第 n 階）
        dp = [0] * (n + 1)

        # XXX 初始條件，要能夠套入「狀態轉移公式」！如下面那樣
        dp[0] = 1  # 到第 0 階的方法數
        dp[1] = 1  # 到第 1 階的方法數

        # 從第 2 階開始計算
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # 套用了初始條件來計算

        # 返回第 n 階的方法數
        return dp[n]
