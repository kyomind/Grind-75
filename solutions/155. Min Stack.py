class MinStack1:
    def __init__(self):
        # 主堆疊，用來儲存所有插入的元素
        self.stack = []
        # 輔助堆疊，用來記錄每個狀態下的最小值
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # 如果輔助堆疊為空，或新插入的元素「小於、等於」當前最小值，則也推入輔助堆疊
        # XXX 輔助堆疊的頂端「總是」堆疊目前的最小值
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        top_element = self.stack.pop()

        # XXX 如果彈出的元素等於輔助堆疊的頂端，則「也」從輔助堆疊中彈出
        # 這樣可以確保輔助堆疊的頂端始終是剩下元素的最小值
        if top_element == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # 直接返回主堆疊的頂端元素
        return self.stack[-1]

    def getMin(self) -> int:
        # 直接返回輔助堆疊的頂端元素，即當前的最小值
        return self.min_stack[-1]

"""
兩個重要的問題與解答(這兩個問題都是兩個堆疊「不同步」才有的議題)

一、為什麼「等於」也要插入？而不是只有小於才插入輔助stack
「等於」的情況下也插入輔助堆疊的原因是為了處理重複的最小值
並在 pop 操作後仍能正確更新最小值

二、為什麼輔助堆疊不會比主堆疊提前耗盡？
當一個元素從主堆疊彈出時，如果該元素不是最小值，輔助堆疊不會發生任何變化
只有當彈出的元素是當前的最小值時，輔助堆疊才會同步彈出該值
"""

# 2025-02-11 採用兩個堆疊同步的寫法
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 可以再化簡，但我覺得不化簡也沒關係
        if self.min_stack:
            min_stack_top = self.min_stack[-1]
            if val < min_stack_top:
                self.min_stack.append(val)
            else:
                self.min_stack.append(min_stack_top)
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        # 這可以通過，顯然測資不會在空堆疊時嘗試top
        return self.stack[-1]

    def getMin(self) -> int:
        # 這可以通過，顯然測資不會在空堆疊時嘗試getMin
        return self.min_stack[-1]
