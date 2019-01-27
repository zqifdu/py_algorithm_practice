"""
Given a non-empty list of words, return the k most frequent elements.

Note: Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
then the word with the lower alphabetical order comes first.
"""
import heapq


def Kmost_frequent(word_list, k):
    if not word_list:
        return []

    n_appear = {word_list[0]: 1}
    heap = [(1, word_list[0])]
    for i in range(1, len(word_list)):
        n_appear[word_list[i]] = n_appear.get(word_list[i], 0) + 1
        if len(heap) < k:
            # If it was in the heap, pop it
            heapq.pop((n_appear[word_list[i] - 1, word_list[i]]))
            # add it to the heap
            heapq.heappush(heap, (n_appear[word_list[i]], word_list[i]))
        else:
            # If it was in the heap, pop it
            heapq.pop((n_appear[word_list[i] - 1, word_list[i]]))
            if len(heap) == k:
                heapq.heappop
