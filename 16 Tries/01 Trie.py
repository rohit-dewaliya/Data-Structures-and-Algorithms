'''
- Insertion in Trie

    - CASE I: Character already exists in current node’s children
        -: Reuse the existing node and move to the next character.

    - CASE II: Character does not exist in current node’s children
        -: Create a new TrieNode for that character and move to it.

    - CASE III: End of word reached
        -: Mark the current node as is_end = True.

    - CASE IV: Word already exists
        -: All characters are found, and is_end is already True → no structural change needed.

- Deletion in Trie
    - CASE I: Some other prefix of string is same as the one that we want to delete(api, apple)
    - CASE II: the string is a prefix of another string (api, apis)
    - CASE III: other string is a prefix of this string (apis, ap)
    - CASE IV: not any node depends on this string
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                node = TrieNode()
                current.children.update({char: node})
            current = node
        current.end = True
        print("Successfully inserted.")

    def search(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                return False
            current = node

        if current.end:
            return True
        return False

    def delete_word(self, word):
        def _delete(root, word, index):
            if index == len(word):
                if not root.end:
                    return False
                root.end = False
                return len(root.children) == 0

            char = word[index]
            current = root.children.get(char)
            can_be_deleted = False

            if len(current.children) > 1:
                _delete(current, word, index + 1)
                return False

            if index == len(word) - 1:
                if len(current.children) >= 1:
                    current.end = False
                    return False
                else:
                    root.children.pop(char)

            if current.end:
                _delete(current, word, index + 1)
                return False

            can_be_deleted = _delete(current, word, index + 1)
            if can_be_deleted:
                root.children.pop(char)
                return True
            else:
                return False

        return _delete(self.root, word, 0)


trie = Trie()
words = ["apple", "app", "apex", "bat", "ball"]
for word in words:
    trie.insert(word)
print(trie.search("apple"))
trie.delete_word("apple")
print(trie.search("apple"))