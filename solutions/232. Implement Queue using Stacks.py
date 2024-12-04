# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 注意，要使用兩個 stack 來實現 queue 的功能，而不是一個 stack
# 涉及平攤時間複雜度(Amortized Time Complexity)的概念
class MyQueue1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用兩個 stack 來實現 queue 的功能
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # 要先檢查 stack_out 是否為空
        # 如果是，就把 stack_in 的元素全部移到 stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # 然後再從 stack_out 中 pop 出元素
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        # 一樣要先檢查 stack_out 是否為空
        # 如果是，就把 stack_in 的元素全部移到 stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # 然後再從 stack_out 中 peek 出元素
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # 確認兩個 stack 是否都為空
        return not (self.stack_in or self.stack_out)
        # 相當於 return self.stack_in == [] and self.stack_out == []


# 2024-12-04
# 主要是peek和pop都是o(n)，要變成o(1)
# 看起來是不必考慮當queue為空時，繼續操作pop或peek發生錯誤的情況
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        # XXX 這裡的檢查條件很重要
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        # 條件與移動操作和pop同
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        # 兩各都空才是空
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
