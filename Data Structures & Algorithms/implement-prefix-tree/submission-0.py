class Node:
    def __init__(self):
        self.childrens = [0] * 26
        self.flag = False

class PrefixTree:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        cur = self.node
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.childrens[idx]:
                cur.childrens[idx] = Node()
            cur = cur.childrens[idx]
        cur.flag = True

    def search(self, word: str) -> bool:
        cur = self.node
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.childrens[idx]:
                return False
            cur = cur.childrens[idx]
        return cur.flag

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for char in prefix:
            idx = ord(char) - ord('a')
            if not cur.childrens[idx]:
                return False
            cur = cur.childrens[idx]
        return True
        