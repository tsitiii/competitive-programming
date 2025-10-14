# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.word = False
        self.children = {}        

    def insert(self, word: str) -> None:
        
        for char in word:
            if char not in self.children:
                self.children[char] = Trie()
            self = self.children[char]
        self.word = True
 
    def search(self, word: str) -> bool:
        for char in word:
            if char not in self.children:
                return False
            self = self.children[char]
        return self.word

    def startsWith(self, prefix: str) -> bool:
        
        for char in prefix:
            if char not in self.children:
                return False
            self = self.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)