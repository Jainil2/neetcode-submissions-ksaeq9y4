class Node:
    def __init__(self):
        self.child = [None] * 26
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.node = Node()

    def addWord(self, word: str) -> None:
        cur = self.node
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = Node()
            cur = cur.child[idx]
        cur.flag = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if not node:
                return False
            if i == len(word):
                return node.flag
            char = word[i]
            if char == '.':
                for child in node.child:
                    if child and dfs(i + 1, child):
                        return True
                return False
            else:
                idx = ord(char) - ord('a')
                return dfs(i + 1, node.child[idx])
        return dfs(0, self.node)
