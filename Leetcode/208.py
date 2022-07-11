class Trie:

    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        root = self.data
        for i, v in enumerate(word, 1):
            if m := root.get(v):
                root = m
            else:
                root[v] = {}
                root = root[v]
        root["word"] = word

    def _search(self, word: str, all=True) -> bool:
        root = self.data
        for v in word:
            if m := root.get(v):
                root = m
            else:
                return False
        if not all: return True if root else False
        return True if root.get("word") == word else False

    def search(self, word: str) -> bool:
        return self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, False)


obj = Trie()
obj.insert("apple")
# assert obj.search("apple") is True
assert obj.search("app") is False
assert obj.startsWith("app") is True
obj.insert("app")
assert obj.search("app") is True
assert obj.search("bapp") is False
assert obj.search("appl") is False
