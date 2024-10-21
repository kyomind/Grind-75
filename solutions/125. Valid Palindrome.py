# 暴力法
class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 將字串轉為小寫，並只保留字母和數字(句子中有包括數字)
        s = "".join([c.lower() for c in s if c.isalnum()])
        # 這行有點 trick，因為 s[::-1] 會回傳 s 的反轉字串，太取巧了
        # - 但我覺得思路不錯，很直觀
        # - 而且同時省去單獨判斷空字串的情況
        return s == s[::-1]


# 雙指針法 - 標準解法
class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        # 我懂了，這個迴圈不是要直接迭代內容，而是要確定迭代次數，而且最多也不會超過 len(s) 次的一半
        for _ in range(len(s)):
            # 如果左指針和右指針指向的字元不是字母或數字，就往中間移動
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # 如果左指針和右指針指向的字元不相等，就回傳 False
            if s[left].lower() != s[right].lower():
                return False
            # 當前字元相同，同時移動左指針和右指針
            left += 1
            right -= 1

            if left >= right:
                return True


# 更好的迴圈終止條件，使用 while 迴圈
def isPalindrome(s: str) -> bool:
    # 初始化兩個指針
    left, right = 0, len(s) - 1

    # 開始迴圈比較——使用while迴圈而不是for迴圈
    # 因為很明顯我們並不是要遍歷整個字串，而是要控制次數而已
    # 上面是用"left>=right"，但反過來用"<"更簡潔
    while left < right:
        # 略過左邊的非字母或數字字串
        while left < right and not s[left].isalnum():
            left += 1
        # 略過右邊的非字母或數字字串
        while left < right and not s[right].isalnum():
            right -= 1

        # 比較兩邊的字串（忽略大小寫）
        if s[left].lower() != s[right].lower():
            return False

        # 移動指針
        left += 1
        right -= 1

    # 若成功遍歷所有字串，則是回文
    return True
