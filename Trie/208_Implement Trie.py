class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            
            curr = curr.children[i]
        curr.isWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
        if(curr.isWord): return True
        else: return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)