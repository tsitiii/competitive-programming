# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class Trie:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.isword = False

class MapSum:
    def __init__(self):
        self.root = Trie()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
            node.value += delta 
        node.isword = True

    def sum(self, prefix: str) -> int:                                         
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.value
