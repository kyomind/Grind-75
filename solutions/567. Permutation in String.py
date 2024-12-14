# 這寫法很難懂，也記不起來
class Solution1:
    def checkInclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 預處理 s1 的字元頻率
        count_s1 = {}
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        # 初始化 S2 上的滑動視窗，這是起始位置
        window_count = {}
        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1

        # 以上都好理解
        # ---
        # 開始滑動視窗，這是用range的寫法，太抽象而且依賴於Python的特性
        for i in range(len(s1), len(s2)):
            if window_count == count_s1:
                return True

            # 移動視窗：新增右邊字元
            right_char = s2[i]
            window_count[right_char] = window_count.get(right_char, 0) + 1

            # 移除左邊字元
            left_char = s2[i - len(s1)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1

        # 最後的視窗比對
        # FIXME 很難理解為何要這樣——為何這是獨立再判斷一次，超怪
        return window_count == count_s1

# 不用 range 的寫法，這樣比較好理解
# 用更通用的 while 寫法來滑動視窗
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 預處理 s1 的字元頻率
        count_s1 = {}
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        # 初始化滑動視窗的字元頻率，與左右邊界(指標)
        window_count = {}
        left = 0  # index 位置
        right = 0
        window_size = len(s1)

        # 滑動視窗，只有左邊界能立刻知曉是不是到盡頭了，所以用 right 作為條件
        while right < len(s2):
            # 開始收集初始化視窗時的字元
            char_right = s2[right]
            window_count[char_right] = window_count.get(char_right, 0) + 1
            right += 1

            # 視窗大小初始化完成
            if right - left == window_size:
                if window_count == count_s1:
                    return True

                # 開始移動視窗，先移除左邊界字元
                # 區分兩種情況：字元頻率為 1 或大於 1
                char_left = s2[left]
                if window_count[char_left] == 1:
                    # 字元頻率為 1 時，移除字典中的 key
                    del window_count[char_left]
                else:
                    # 字元頻率大於 1 時，減少頻率
                    window_count[char_left] -= 1
                left += 1

        # 全部視窗都比對完了，沒有找到
        return False
