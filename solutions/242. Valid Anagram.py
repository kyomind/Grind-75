# 暴力法
class Solution1:
    def isAnagram(self, s, t):
        # 如果兩個字串長度不同，則不可能是 Anagram
        if len(s) != len(t):
            return False

        # 還有每個字母出現的次數也要相同
        # 雖然這寫法太過依賴 Python 的內建函數，但是這裡是為了展示暴力法
        # 本來還打算用字典存放每個字母出現的次數，但顯然不如這樣簡潔(因為用了count)
        for char in set(s):
            if s.count(char) != t.count(char):
                return False

        return True


# 低階一點，使用python的字典 (dict) 來存放每個字母出現的次數
# 不准用字串的 count 方法
# 2024-11-30 迭代一次，使用兩個計數器
class Solution2:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # 這裡用字典存放每個字母出現的次數
        s_dict = {}
        t_dict = {}

        # range(len(s)) 這樣寫不夠 pythonic
        for i, _ in enumerate(s):
            # get 中的 0 是初始化值，如果字典中沒有這個 key，就會返回 0
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict


# 再低階一點，使用 list 來存放每個字母出現的次數
# 2024-11-30 迭代兩次，使用一個計數器
class Solution3:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # 這裡用 list 存放每個字母出現的次數
        count_list = [0] * 26

        for i in range(len(s)):
            # 必須減去ord('a')，才能將字母映射到0-25的範圍
            # 讓兩者相互抵銷，每一個字母出現一次，就加一次，出現一次就減一次
            # 結果必須是全為0
            count_list[ord(s[i]) - ord("a")] += 1
            count_list[ord(t[i]) - ord("a")] -= 1

        for count in count_list:
            if count != 0:
                return False

        return True


# 2024-11-30 先用雜湊計數就好，不搞排序
# 迭代兩次，只建立一個計數器
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # XXX 第一個問題：怎麼同時迴圈兩個字串？
        # 答案是不必，先迭代其中一個即可
        # XXX 而且要使用+-相互抵消的方式來做，不要用兩個字典了！
        count = {}
        for i in s:
            # 搞笑的低級錯誤 count.get(i, 0) += 1
            count[i] = count.get(i, 0) + 1

        for i in t:
            # 還是需要預設值0，防止兩者並非字母異位詞（anagram）
            count[i] = count.get(i, 0) - 1

        for v in count.values():
            if v != 0:
                return False

        # 更簡單且仍算很好懂的寫法
        # all、any 我覺得就不要了，常常忘記定義
        # if sum(count.values()) != 0:
        #     return False

        return True
