# Leetcode problem 899

def orderlyQueue(S, K):
    if K == 1:
        # comprehensive can be used in min/max functions
        return min(S[i:] + S[:i] for i in range(len(S)))
    # sorted() can order a string in lexicographical order but will return a list, that's why "".join is needed
    return "".join(sorted(S))

if __name__ == '__main__':
    a = 'daofenoifnonaeqnrio'
    K = 1
    print(orderlyQueue(a, K))
    K = 2
    print(orderlyQueue(a, K))