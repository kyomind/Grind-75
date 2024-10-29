# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    """This function is already defined in the problem"""
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 這裡的數字和 index 無關，只是用來表示版本號
        # 所以直接從 1 開始
        left = 1  # 左邊界
        right = n  # 右邊界

        # 使用 while left < right 讓迴圈自然結束，是更常見的寫法
        # while True 的話就一定要有停止條件: break 或 return
        while True:
            # 定義中間值，這裡的 mid 是版本號
            mid = left + (right - left) // 2
            # 相當於 mid = (left + right) // 2
            # 這樣寫是為了避免 left + right 過大而溢位
            # 雖然在 Python 中不會溢位，但是這樣寫是一個好習慣

            if isBadVersion(mid):
                # 如果是壞版本，表示第一壞版本在左半邊
                # 將右邊界設為 mid
                right = mid

            else:
                # 如果不是壞版本，表示第一壞版本在右半邊
                # 將左邊界設為 mid+1
                left = mid + 1

            # 當左邊界等於右邊界時，表示找到第一個壞版本
            if left == right:
                return left


"""
Q：為何其中一個需要+1但另外一個不用呢？

當 isBadVersion(mid) 返回 True 時，mid「可能」是第一個壞版本（也可能不是），
因此我們需要繼續檢查 mid 的左邊（包括 mid 本身），所以 right 設為 mid。

當 isBadVersion(mid) 返回 False 時，mid 不是壞版本，
因此第一個壞版本「一定」在 mid 的右邊，所以 left 設為 mid + 1。

這樣的邏輯保證了我們不會錯過任何可能的壞版本，並且能夠在最短的時間內找到第一個壞版本。
"""
