class Solution1(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 無恥做法，直接使用Python str的count方法
        # 答案是不行，因為這樣子沒有考慮到順序變化的問題，不同順序也是合法的
        # 比如說 ransomNote = "aab", magazine = "aba"
        return magazine.count(ransomNote) > 0


# 可以 work，但效能很爛，只能 beat 7% 左右
class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 還是繼續用count耍賤，但做法要稍稍變一下
        for c in ransomNote:
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True


# 用 dict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # ai 寫的，暴力法，感覺不夠優雅
        # 效能上也只有 beat 45%
        count = {}
        for c in magazine:
            count[c] = count.get(c, 0) + 1
        for c in ransomNote:
            # XXX 我覺得這段值得一看，在減到0之後，就會回傳False
            # 表示這個字母不夠用了
            # 我喜歡這個思路，但自己可能不容易想到
            if count.get(c, 0) == 0:
                return False
            count[c] -= 1
        return True