# 暴力法，但不可行，因為無法處理 "([)]" 這種情況
class Solution1:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_map = {")": 0, "]": 0, "}": 0, "(": 0, "[": 0, "{": 0}
        for c in s:
            if c == "(":
                char_map["("] += 1
            elif c == ")":
                char_map[")"] += 1
            elif c == "[":
                char_map["["] += 1
            elif c == "]":
                char_map["]"] += 1
            elif c == "{":
                char_map["{"] += 1
            elif c == "}":
                char_map["}"] += 1
        if (
            char_map["("] != char_map[")"]
            or char_map["["] != char_map["]"]
            or char_map["{"] != char_map["}"]
        ):
            return False
        return True


# 使用 stack
class Solution2:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                # 如果已經是空的，就不用再檢查了，不然 pop 下去會出現 IndexError
                # XXX 2024-11-27 忘記這個確認
                if not stack:
                    return False
                if c == ")" and stack[-1] != "(":
                    return False
                if c == "]" and stack[-1] != "[":
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        # 不只過程中要檢查是否為空，全部結束後，也要檢查是否為空
        # 以下寫法相當於 return not stack——但這種一行式的寫法不好懂
        if stack:
            return False
        return True


# 2024-11-27
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
            # 這裡可以確定，當前的 i 是結束符號，要從stack拉出一個對應的
            # 而且要剛好對應——大對大、中對中、小對小，不可以對錯
            else:
                if not stack:
                    return False
                # 寫法不優雅，就是線性思考而已
                if i == "}" and stack.pop() == "{":
                    continue
                if i == "]" and stack.pop() == "[":
                    continue
                if i == ")" and stack.pop() == "(":
                    continue
                else:
                    return False

        if stack:
            return False
        return True
