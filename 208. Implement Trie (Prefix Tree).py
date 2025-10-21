class Trie:

    def __init__(self):
        self.initial = Node()

    def insert(self, word: str) -> None:
        node = self.initial
        for char in word:
            if char not in node.children:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
            else:
                node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.initial
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.initial
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Node:

    def __init__(self, char = ''):
        self.char = char
        self.is_word = False
        self.children = dict()

    def __repr__(self):
        return f'char is {self.char} and children are {self.children}'

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)