# 本題的重點是回溯法 (backtracking)
# 有帶迴圈和不帶迴圈的兩種解法
# 初學者建"不帶迴圈"的解法開始學習，因為比較直觀

# XXX 注意，解法中使用了 closure 的概念
# - 將result陣列放在外部，並直接在helper函數中使用
# - nums也是直接在helper函數中使用
# 這樣可以減少參數傳遞，提高效率
class Solution:
    # 不使用迴圈的解法 by ChatGPT
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            # 停止條件，已到達陣列尾部
            if index == len(nums):
                result.append(current[:])
                return

            # 不選擇當前元素，遞迴到下一層
            backtrack(index + 1, current)

            # 選擇當前元素，遞迴到下一層
            current.append(nums[index])
            backtrack(index + 1, current)

            # 回溯，撤回選擇
            current.pop()

        # 初始遞迴從索引 0 開始
        backtrack(0, [])
        return result
