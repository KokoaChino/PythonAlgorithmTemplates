class TrieNode: # 字典树节点
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie: # 字典树
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str): # 插入单词
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_word = True

    def search_prefix(self, word: str) -> TrieNode(): # 查找前缀
        p = self.root
        for c in word:
            if c not in p.children:
                return None
            p = p.children[c]
        return p

    def search(self, word: str) -> bool: # 查找单词
        p = self.search_prefix(word)
        return p is not None and p.is_word