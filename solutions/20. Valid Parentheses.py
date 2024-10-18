# 暴力法，但不可行，因為無法處理 "([)]" 這種情況
class Solution(object):
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
class Solution2(object):
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
                # 如果已經是空的，就不用再檢查了，不然會出現 IndexError
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
        if stack:
            return False
        return True
        # 相當於 return not stack，但這種一行式的寫法不好懂