"""
https://www.lintcode.com/problem/word-break-ii/
"""


# My solution version 1
class trie_node:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word = ""


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        word_trie_root = self.build_trie(wordDict)
        ans = []
        ind_word_dict = dict()
        self.dfs(s, word_trie_root, 0, ans, [], ind_word_dict)

        return ans

    def dfs(self, s, word_trie_root, start, ans, words, ind_word_dict):
        if start == len(s):
            print(words)
            ans.append(" ".join(words))
            return

        if start in ind_word_dict:
            next_words = ind_word_dict[start]
        else:
            # Search through the word_trie
            next_words = []
            curr_node = word_trie_root
            for char_ind in range(start, len(s)):
                char = s[char_ind]
                found_in_child = False
                for child in curr_node.children:
                    if char == child.char:
                        found_in_child = True
                        if child.word != "":
                            next_words.append(child.word)
                        curr_node = child
                        break
                if not found_in_child:
                    break
            ind_word_dict[start] = next_words
            print(start, ind_word_dict[start])

        if not next_words:
            return

        for next_word in next_words:
            self.dfs(s, word_trie_root, start + len(next_word), ans, words + [next_word],
                     ind_word_dict)

    def build_trie(self, wordDict):
        root = trie_node("")

        for word in wordDict:
            curr_node = root
            for char in word:
                char_node_exist = False
                for child in curr_node.children:
                    if char == child.char:
                        char_node_exist = True
                        curr_node = child
                        break
                if not char_node_exist:
                    new_node = trie_node(char)
                    curr_node.children.append(new_node)
                    curr_node = new_node

            curr_node.word = word
        return root

# test cases
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

sol = Solution()
print(sol.wordBreak(s, wordDict))
