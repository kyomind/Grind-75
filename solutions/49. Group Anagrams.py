# 字典計數法
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 總計數字典，key是所有字串的字母計數array，value是所有符合該計數array的字串
        # 了解這個格式非常重要！
        counter = {}
        # 為每一個字串建立屬於它的key，key的內容是字母的計數array
        for s in strs:
            # 初始化字母計數array
            count = [0] * 26  # 最多26個字母
            # 計算字母計數array
            for c in s:
                count[ord(c) - ord("a")] += 1
            # 算完後，count的example: [1, 0, 0, 0, 1...]

            # 轉換成tuple，才能作為字典的key，這是因為list是不可hash的
            key = tuple(count)  # ex: (1, 0, 0, 0, 1...)

            # 如果key不存在，則初始化一個空list，以免後面的append出錯，存在就不用管
            if key not in counter:
                counter[key] = []
            # 將字串加入對應的key
            counter[key].append(s)

        # 最後，將所有value取出，就是答案
        return list(counter.values())  # 不要忘記轉換成list


# 無註解簡潔版
def groupAnagrams(strs):
    anagram_dict = {}
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1

        key = tuple(count)

        if key not in anagram_dict:
            anagram_dict[key] = []
        anagram_dict[key].append(s)

    return list(anagram_dict.values())
