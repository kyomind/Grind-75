# 本題是經典的滑動視窗問題
# 可以用字典或集合來記錄當前子串中的字元


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        字典法→更加優雅，但是理解的負擔更大(較為抽象)
        因為字典中的值，即索引，已經巧妙地控制了目前視窗的大小
        """
        # 用來記錄字元上次出現的位置
        char_index = {}
        # 用來記錄當前子串的起始位置
        start = 0
        # 用來記錄最長子串的長度
        max_length = 0
        for i, char in enumerate(s):
            # 如果字元已經出現過，則更新起始位置
            if char in char_index:
                start = max(start, char_index[char] + 1)

            # 更新字元的位置
            char_index[char] = i

            # 更新最長子串的長度
            max_length = max(max_length, i - start + 1)
        return max_length


class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        集合法→更基本的做法
        只是遇到重複字元時，需要用 while 迴圈來更新起始位置
        """
        # 用來記錄當前子串的字元
        char_set = set()
        # 用來記錄當前子串的起始位置
        start = 0
        # 用來記錄最長子串的長度
        max_length = 0
        for i, char in enumerate(s):
            # 如果字元已經出現過，則更新起始位置
            # 如果重複字元在當前子字串的中段或後段，需要多次移動 left 指針，所以會用 while 迴圈
            while char in char_set:
                char_set.remove(s[start])
                start += 1

            # 更新字元的位置
            char_set.add(char)
            # 更新最長子串的長度

            max_length = max(max_length, i - start + 1)
        return max_length
