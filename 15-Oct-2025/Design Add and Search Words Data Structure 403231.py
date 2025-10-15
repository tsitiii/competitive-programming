# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

    
class WordDictionary:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.isword = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.isword
            char = word[i]
            if char == '.':
                for child in root.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in root.children:
                    return False
                return dfs(root.children[char], i + 1)
                
        return dfs(self,0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()                                                                                                                                                                                                        
# obj.addWord(word)
# param_2 = obj.search(word)