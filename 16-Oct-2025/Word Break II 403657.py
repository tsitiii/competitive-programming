# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Trie:
    def __init__(self):
        self.children ={}
        self.isword = False
class Solution:
    def __init__(self):
        self.root = Trie()
    
    def addword(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = Trie()
                node = node.children[char]
            node.isword = True
    def search(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.isword

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        for word in wordDict:
            self.addword(word)
        result = []
        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if self.search(word):
                    backtrack(end, path + [word])
        backtrack(0, [])
        return result

    