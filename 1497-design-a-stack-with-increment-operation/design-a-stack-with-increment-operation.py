from collections import deque
class CustomStack:

    def __init__(self, maxSize: int):
        self.s = deque()
        self.max_size = maxSize
        self.currSize = 0

    def push(self, x: int) -> None:
        if self.currSize < self.max_size:
            self.s.append(x)
            self.currSize += 1
        

    def pop(self) -> int:
        if self.currSize > 0:
            self.currSize -= 1
            return self.s.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.currSize)):
            self.s[i] += val




# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)