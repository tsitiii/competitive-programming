# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        self.head = Node()  
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node_to_head(self, node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_node_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_node_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_node_to_head(node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

# Example Usage (as provided in the prompt):
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)