# 本題是經典的滑動視窗問題
# 可以用字典或集合來記錄當前子串中的字元


class Solution3:
    def lengthOfLongestSubstring(self, s):
        """
        字典法→更加優雅，但是理解的負擔更大(較為抽象)
        因為字典中的值，即索引，已經巧妙地控制了目前視窗的大小
        """
        # 用來記錄字元上次出現的位置
        char_last_seen_index = {}
        # 用來記錄當前子串的起始位置
        left = 0  # 滑動視窗左邊界
        # 用來記錄最長子串的長度
        max_length = 0
        for right, char in enumerate(s):
            # 如果字元已經出現過，則更新起始位置
            if char in char_last_seen_index:
                left = max(left, char_last_seen_index[char] + 1)

            # 更新字元的位置
            # XXX 這個操作其實就是存下目前的index和char內容而已，沒什麼特別
            # 這個位置會比之前的更新，所以變動的是index，也就是right的值
            char_last_seen_index[char] = right

            # 過程中，不斷確認、更新最長子串的長度
            max_length = max(max_length, right - left + 1)
        return max_length


class Solution11:
    def lengthOfLongestSubstring(self, s):
        """
        集合法→更基本的做法
        只是遇到重複字元時，需要用 while 迴圈來更新起始位置 left
        """
        # 用來記錄當前子串的字元
        char_set = set()
        # 用來記錄當前子串的起始位置
        left = 0
        # 用來記錄最長子串的長度
        max_length = 0
        for right, char in enumerate(s):
            # 如果字元已經出現過，則更新起始位置
            # 如果重複字元在當前子字串的中段或後段，需要多次移動 left 指針，所以會用 while 迴圈
            while char in char_set:
                """
                這裡的一大重點是，當char已經在set中時，那就要讓當前這個char去取代過去的相同值
                此時要移動left指針，如果移動一次，set中的char就沒了
                - 那就可以繼續把當前的加進來，此時的差別是left指針移動了
                但如果一次還不夠，就是移動多次，但最終當前的char還是會加進來set
                - 移動多次並不是因為有多個重複(事實上只會有一個重複)
                - 而是移動一次，還無法消除重複，而需要移動多次
                """
                # XXX 必須移除元素，不然 while 是「無限」迴圈
                # 雖然脫離迴圈後，又立刻加回集合中了，但先脫離是必要條件
                char_set.remove(s[left])
                left += 1

            char_set.add(char)  # 又加回來了，但這次是因為最新的字元
            max_length = max(max_length, right - left + 1)  # 注意這個+1，因為是兩邊都要包括
        return max_length


# 2025-02-05 重要！
# XXX 不要用 enumerate
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        char_set = set()
        left = 0
        right = 0
        max_length = 0
        for char in s:
            while char in char_set:
                # XXX 錯誤且重要：char_set.remove(char)
                # 難怪我想說，怎麼沒有「從左邊開始移除字元的感覺？」果然是寫錯了！
                char_set.remove(s[left])
                left += 1

            char_set.add(char)
            max_length = max(max_length, right - left + 1)
            right += 1  # XXX 錯誤：本來這行寫在上一行之前，就錯了
            # 因為要本次 for 的邏輯全算完，最後才能移動 right 指針
            # right +1，是下一次的迴圈的狀態，不是本次
            # 這個如果用 enumerate，就你不可能會發生這個情況，因為會是在下一次起始時才會+完1
            # 太習慣 enumerate 可能不是好事

        return max_length
