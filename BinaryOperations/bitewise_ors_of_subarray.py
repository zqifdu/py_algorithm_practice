# Leetcode problem 898

def subarrayBitwiseORs(A):
    ans = set()
    cur = {0}
    for x in A:
        cur = {x | y for y in cur} | {x}
        ans |= cur
    return len(ans)


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    ans = subarrayBitwiseORs(A)
