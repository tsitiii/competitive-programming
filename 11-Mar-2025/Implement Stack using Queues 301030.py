# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.front = deque()
        self.back = []
        self.dq = deque()
    def push(self, x: int) -> None:
        self.dq.append(x)
    def pop(self) -> int:
        return self.dq.pop()

    def top(self) -> int:
        return self.dq[-1]

    def empty(self) -> bool:
        if not self.dq:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()