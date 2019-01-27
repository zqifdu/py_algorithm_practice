# From https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter


def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for v in arr:
        if v in r3:
            count += r3[v]

        if v in r2:
            r3[v * r] += r2[v]

        r2[v * r] += 1

    return count

