class Solution:
    def evalRPN(self, tokens):
        # 初始化一個空的堆疊，用來儲存操作數和中間結果
        stack = []

        # 遍歷所有的 token
        for token in tokens:
            if token in {"+", "-", "*", "/"}:  # token 為運算符
                # 從堆疊中彈出兩個操作數字
                b = stack.pop()  # XXX 注意：基於 stack 特性，先彈出的是第二個操作數，這是一大重點！
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
                    # 不能用「//」因為它是向負無窮取值，在負數時不符合需求
                    result = int(a / b)

                # 將計算結果壓回堆疊
                stack.append(result)

            else:  # token 為數字
                stack.append(token)

        # 堆疊中最後剩下的唯一元素即為計算結果
        return stack[0]
