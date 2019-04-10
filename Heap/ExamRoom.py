import collections
import heapq
import bisect


class ExamRoom_bin:
    def __init__(self, N: int):
        self.n = N
        self.students = []

    def seat(self):
        if not self.students:
            student = 0
        else:
            # initialize the new distance and position
            dist, student = self.students[0], 0
            # loop through all the intervals
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # calculate the new distance
                    d = (s - prev)//2
                    # if the new distance is larger, then we prefer the new position
                    if d > dist:
                        dist, student = d, s
        # edge case: the right-most position
        d, s = self.N - 1 - self.students[-1], self.students[-1]
        if d > dist:
            dist, student = d, s
        # Insert the new position into the sorted positions
        bisect.insort_left(self.students, student)

    def leave(self, p):
        self.students.remove(p)



class ExamRoom:
    def __init__(self, N: int):
        self.n = N
        self.heap = []
        self.right = collections.defaultdict(int)
        self.left = collections.defaultdict(int)
        self._push(0, self.n - 1)

    def _push(self, l, r):
        """
        Push an interval into the heap
        """
        # push an interval to the heap
        if r >= l:
            width = -((r - l) // 2)  # -5//2 = -3, -(5//2) = 2
            # edge case: ends of an interval is available
            if l == 0 or r == self.n - 1:
                width = l - r
            # update the right map and left map used to determine if an interval is valid
            self.right[l] = r
            self.left[r] = l
            # push the interval into the heap
            heapq.heappush(self.heap, (width, l, r))

    def _pop(self):
        """
        heappop an interval from the heap
        """
        if len(self.heap) == 0:
            return None
        # pop the interval with max-closest distance with neighbor
        w, l, r = heapq.heappop(self.heap)
        if not self.right[l] == r:  # invalid interval
            # keep popping untill valid
            return self._pop()
        return (w, l, r)

    def seat(self) -> int:
        # Find the largest valid interval to seat a student
        w, l, r = self._pop()
        t = (l + r) // 2
        if l == 0:
            t = 0
        elif r == self.n - 1:
            t = r
        # Push the new intervals to the heap
        self._push(l, t - 1)
        self._push(t + 1, r)
        # There should be no interval involving the current position, mark it with -1
        self.left[t] = -1
        self.right[t] = -1
        return t

    def leave(self, p: int) -> None:
        l, r = None, None
        # Find out the new interval to push into the heap due to the leaving of p
        if p == 0:
            l = 0
        else:
            if self.left[p - 1] != -1:
                l = self.left[p - 1]
            else:
                l = p

        if p == self.n - 1:
            r = self.n - 1
        else:
            if self.right[p + 1] != -1:
                r = self.right[p + 1]
                self.right[p + 1] = 0
            else:
                r = p
        self._push(l, r)


em = ExamRoom(10)
print(em.heap)
print(em.right)
print(em.left)


em.seat()
print(em.heap)
print(em.right)
print(em.left)


em.seat()
print(em.heap)
print(em.right)
print(em.left)

em.seat()
print(em.heap)
print(em.right)
print(em.left)

em.leave(0)
print(em.heap)
print(em.right)
print(em.left)

em.seat()
print(em.heap)
print(em.right)
print(em.left)