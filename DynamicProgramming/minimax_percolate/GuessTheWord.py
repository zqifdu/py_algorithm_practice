"""
https://leetcode.com/problems/guess-the-word/solution/
"""


# My own solution
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        start_word1 = wordlist[0]
        start_word2 = wordlist[1]

        overlap1 = master.guess(start_word1)
        overlap2 = master.guess(start_word2)

        candidates1 = set()
        candidates2 = set()
        for i in range(2, len(wordlist)):
            if sum(1 if c1 == c2 else 0 for c1, c2 in zip(start_word1, wordlist[i])) == overlap1:
                candidates1.add(wordlist[i])
            if sum(1 if c1 == c2 else 0 for c1, c2 in zip(start_word2, wordlist[i])) == overlap2:
                candidates2.add(wordlist[i])

        candidates1 = candidates1 & candidates2
        guess_quota = 8

        while len(candidates1) > guess_quota and guess_quota > 0:
            candidate_list = list(candidates1)
            new_start_word = candidate_list[0]
            overlap_new = master.guess(new_start_word)
            candidate_new = set()
            for i in range(1, len(candidate_list)):
                if sum(1 if c1 == c2 else 0 for c1, c2 in zip(new_start_word, candidate_list[i])) == overlap_new:
                    candidate_new.add(candidate_list[i])
            candidates1 &= candidate_new
            guess_quota -= 1

        candidate_list = list(candidates1)
        for i in range(len(candidate_list)):
            master.guess(candidate_list[i])


# minimax solution
# 直觉理解：
# 比如一个四个词，第一个跟另外三个的overlap 是 2, 2, 1， 第二个跟另外三个是 2, 3, 4
# 那么肯定选第二个，因为第一个词 guess 一下最多还有两个 candidates
# 但是第二个词 guess 一下最多只剩一个
# 所以每次选择是看跟其他词 most frequent overlap 出现的数量最小的那个

import itertools


class Solution(object):
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in itertools.izip(wordlist[i], wordlist[j]))
                   for j in range(N)] for i in range(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess