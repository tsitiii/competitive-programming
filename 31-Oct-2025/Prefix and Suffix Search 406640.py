# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                prefix = word[:i]
                for j in range(n + 1):
                    suffix = word[j:]
                    key = prefix + '#' + suffix
                    self.trie[key] = idx

    def f(self, pref: str, suff: str) -> int:
        key = pref + '#' + suff
        return self.trie.get(key, -1)