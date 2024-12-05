# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    """This function is already defined in the problem"""
    pass


class Solution1:
    def firstBadVersion(self, n):
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


# 2024-12-05
# 一律採用雙閉區間
class Solution:
    def firstBadVersion(self, n: int):
        # XXX 注意，這裡不是index，所以很單純！
        left = 1
        right = n
        # XXX 依題意，本題「一定」有壞版本，所以不會出現目標不存在(基本題的 target index 為 -1)
        # 那直接無限迴圈然後在找到答案後靠 return 結束即可
        while True:
            # mid = left + right // 2 錯誤 FIXME
            mid = (left + right) // 2
            if isBadVersion(mid):
                # mid是壞，第一壞版本在前半，縮小後半邊界至mid
                right = mid
            else:
                # mid正常，第一壞在後半，縮小前半邊界至mid+1
                # mid正常，絕對不是答案了
                # XXX 必須 mid +1，不然可能會無限迴圈，詳筆記！
                left = mid + 1

            # FIXME 結束條件不清楚！寫成這樣
            # if mid == left: 錯誤
            if left == right:
                #   return mid 錯誤
                return left
            """
            不變性原則
            不變性（Invariant）：每次迭代後，範圍 [left, right] 都包含至少一個壞版本。
            當範圍縮小到只有一個元素（left == right），該元素必然是 第一個壞版本。
            """


# 下次不使用無限迴圈，改用正規做法，讓觀念更清楚
