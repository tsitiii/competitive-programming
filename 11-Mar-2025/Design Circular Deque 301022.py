# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if len(self.dq) == self.dq.maxlen:
            return False
        else:
            if not self.dq:
                self.dq.append(value)
            else:
                self.dq.appendleft(value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq) == self.dq.maxlen:
            return False
        else:
            self.dq.append(value)
            return True

    def deleteFront(self) -> bool:
        if not self.dq:
            return False
        else:
            self.dq.popleft()
            return True

    def deleteLast(self) -> bool:
        if not self.dq:
            return False
        else:
            self.dq.pop()
            return True

    def getFront(self) -> int:
        if not self.dq:
            return -1 
        else:
            return self.dq[0]

    def getRear(self) -> int:
        if not self.dq:
            return -1 
        else:
            return self.dq[-1]

    def isEmpty(self) -> bool:
        if not self.dq:
            return True
        else:
            return False

    def isFull(self) -> bool:
        return len(self.dq) == self.dq.maxlen 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()