def getIndex(A):
    stack = [0]
    left = [-1] * len(A)
    for i in range(1,len(A)):
        if A[i] > A[stack[-1]]:
            left[i] = stack[-1]
        else:
            while stack and A[i] <= A[stack[-1]]: stack.pop()
            if not stack: left[i] = -1
            else: left[i] = stack[-1]
        stack.append(i)
    return left

A = [3, 2, 1, 4, 5, 2, 7, 3]

getIndex(A)