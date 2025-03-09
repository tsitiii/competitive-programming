# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = []
        self.count_value = 0  

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count_value += 1
        
        if len(self.queue) > self.k:
            oldest_num = self.queue.pop(0)
            if oldest_num == self.value:
                self.count_value -= 1

        return len(self.queue) == self.k and self.count_value == self.k