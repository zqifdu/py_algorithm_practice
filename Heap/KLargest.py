import heapq


def kth_largest(A, k):
    heap = []
    for i in range(k):
        heap.append(A[i])

    # Maintain a Min-heap
    heap = heapq.heapify(heap)
    for i in range(k, len(A)):
        if A[i] <= heap[0]:
            continue
        else:
            heapq.heappop(heap)
            heapq.heeappush(heap, A[i])

    return heapq[0]
