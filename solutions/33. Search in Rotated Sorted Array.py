class Solution1:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 雙閉區間 [left, right]，所以條件是 left <= right
        # XXX 雙閉區間，所以 mid 的移動是 +1 和 -1
        while left <= right:  # 搜尋範圍是 [left, right]，因此終止條件是 left > right
            """使用 while left <= right 作為迴圈條件
            表示只要搜尋範圍 [left, right] 還有可能包含目標值，就繼續進行
            雙閉區間，兩者有重疊的可能，當 left == right 時，仍然需要進行一次迭代
            這樣可以保證退出迴圈時，left 和 right 會停在一個位置，並且 left > right
            """
            mid = left + (right - left) // 2  # 計算中間索引，同時避免溢位
            # 相當於 mid = (left + right) // 2

            # 判斷是否已找到目標值
            if nums[mid] == target:
                return mid  # 返回目標值的索引

            # XXX 判斷哪一部分是有序的，這是解題的關鍵
            # 2025-02-09 通常會獨立一組if/else，這裡是合理的
            if nums[left] <= nums[mid]:  # 確認左半部分 [left, mid] 是有序的
                if nums[left] <= target < nums[mid]:
                    # 如果目標值在左半部分範圍內，縮小到左半部分
                    right = mid - 1
                else:
                    # 否則，目標值在右半部分
                    left = mid + 1
            else:  # 否則右半部分 [mid, right] 是有序的
                if nums[mid] < target <= nums[right]:
                    # 如果目標值在右半部分範圍內，縮小到右半部分
                    left = mid + 1
                else:
                    # 否則，目標值在左半部分
                    right = mid - 1

        # 如果退出迴圈，表示目標值不存在
        return -1


# 2025-02-09
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:  # 依題意與目標，這行應該不會執行的
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            # XXX mid 必須在迴圈內，因為它要受左右更新的影響而不斷更新
            mid = (left + right) // 2
            if nums[mid] == target:  # XXX 其實這if有衛語句的效果，有就return，少了一層巢狀！
                return mid

            # 判斷mid左右的哪一邊是有序的
            # XXX 注意，必須使用"<="才能正確判斷，只有"<"會出現錯誤！
            if nums[left] <= nums[mid]:  # left邊有序，可以繼續處理
                # 判斷 target 在不在這個left邊範圍內，用邊界比較即可
                if nums[left] <= target < nums[mid]:  # yes，這是最佳結果，有序+yes
                    # 回歸普通的二元搜尋
                    right = mid - 1
                else:  # no，一樣可以縮小範圍，但另一邊還包括了反轉點
                    left = mid + 1

            else:  # right邊有序，做差不多的事！只是左右的邏輯略有不同而已
                # 判斷 target 在不在這個right邊範圍內
                if nums[mid] < target <= nums[right]:  # yes
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# 以下只要寫出上面一樣的模式即可
