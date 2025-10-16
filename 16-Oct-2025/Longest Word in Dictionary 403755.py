# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.children = {}
        self.isword = False

class Solution:
    def __init__(self):
        self.root = Trie()
    def addword(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isword = True
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children or not node.children[ch].isword:
                return False
            node = node.children[ch]
        return True
    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.addword(word)
        best = ""
        for word in words:
            if self.search(word):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best