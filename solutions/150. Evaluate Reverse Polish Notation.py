class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]  # 這裡的 tokens 都是字串
        :rtype: int
        """
        # 初始化一個空的堆疊，用來儲存操作數和中間結果
        stack = []

        # 遍歷所有的 token
        for token in tokens:
            # 如果 token 是運算符
            if token in {"+", "-", "*", "/"}:
                # 從堆疊中彈出兩個操作數
                b = stack.pop()  # XXX 注意：基於 stack 特性，先彈出的是第二個操作數
                a = stack.pop()  # 後彈出的是第一個操作數

                # 根據不同的運算符進行計算
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    # 整數除法向零截斷，使用 int(a / b) 確保符合題目需求
                    result = int(a / b)

                # 將計算結果壓回堆疊
                stack.append(result)

            else:
                # 如果 token 是數字，則轉換為整數後壓入堆疊
                stack.append(int(token))

        # 堆疊中最後剩下的唯一元素即為計算結果
        return stack[0]
