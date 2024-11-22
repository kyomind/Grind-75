class Solution1:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


"""
本題的程式碼真的非常簡潔優雅，只能說這個題目設計得太精妙了。
這個題目的解法是使用雙指針，一個指向陣列的左端，另一個指向陣列的右端。
然後，我們計算這兩個指針所指向的容器的面積，並更新最大面積。
接著，我們移動指向較小高度的指針，以尋找更高的高度。
這樣，我們就可以在 O(n) 的時間複雜度內解決這個問題。
"""


# 有註解的版本
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 初始化兩個指針，分別指向陣列的兩端
        left, right = 0, len(height) - 1
        # 初始化最大面積為 0
        max_area = 0

        # 開始雙指針迴圈，直到兩指針相遇
        while left < right:
            # 計算當前容器的面積
            current_area = min(height[left], height[right]) * (right - left)
            # 更新最大面積
            max_area = max(max_area, current_area)

            # 判斷移動哪個指針
            if height[left] < height[right]:
                # 左指針指向的高度較小，移動左指針以尋找更高的高度
                left += 1
            else:
                # 右指針指向的高度較小或相等，移動右指針
                right -= 1

        # 返回最終的最大面積
        return max_area
