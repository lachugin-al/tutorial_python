# Резюме 7-го урока курса по алгоритмам и структурам данных

"""
На 7-м уроке были пройдены следующие темы:
1. что такое стэк? Реализация с помощью list
2. что такое дек? Реализация с помощью collections.deque
3. что такое очередь? Реализация с помощью collections.deque
4. решение "Valid Parentheses" https://leetcode.com/problems/valid-parentheses/
5. решение "739. Daily Temperatures" https://leetcode.com/problems/daily-temperatures/
6. решение "239 Sliding Window Maximum" https://leetcode.com/problems/sliding-window-maximum/
"""


""" 1. Что такое стэк? Реализация с помощью list """


# Stack - стэк
# push - добавить элемент на вершину стэка, O(1)
# pop - удалить элемент с вершины стэка, O(1)
# top - посмотреть элемент на вершине стэка, O(1)
# empty - пустой ли стэк? O(1)
# size - размер стэка O(1)
# Не позволяет обратиться к элементу по индексу,
# т.е. вы не можете сделать stack[index].

# LIFO - Last-in First-out

stack = []

# append == push
stack.append(10)
stack.append(20)
stack.append(15)

# pop == pop
stack.pop()

# top == list[-1]
stack[-1]

# empty
len(stack) == 0

# size
len(stack)


""" 2. Что такое дек? Реализация с помощью collections.deque """
""" 3. Что такое очередь? Реализация с помощью collections.deque """


# Queue - очередь
# FIFO - First-in First-out
# push - добавить элемент в конец очереди O(1)
# pop - вытащить первый элемент в очереди O(1)
# empty - пустая ли очередь? O(1)
# size - размер очереди O(1)
# front - элемент в самом начале очереди O(1)
# В C++ нельзя было посмотреть элемент по индексу.

# Deque - двусторонняя очередь, дек
# push_back - добавить элемент в конец очереди O(1)
# push_front - добавить элемент в начало очереди O(1)
# pop_back - удалить элемент с конца очереди O(1)
# pop_front - удалить элемент с начали очереди O(1)
# empty - пустой ли дек O(1)
# size - размер дека O(1)
# front - первый в очереди элемент O(1)
# back - последний в очереди элемент O(1)
# В C++ можно было посмотреть элемент по индексу.

from collections import deque

# class collections.deque([iterable[, maxlen]])
q = deque()
d = deque()

# queue, deque, push - append

q.append(1)
q.append(2)
q.append(3)

d.append(4)
d.append(5)
d.append(6)

# queue, pop == popleft()

print(q.popleft())
print(q)

print(d.pop())
print(d)

print(d.popleft())
print(d)

d.appendleft(7)
print(d)

# size
print(len(d))

# empty
print(len(d) == 0)

# front
print(d[0])

# back
print(d[-1])


""" 4. Решение "Valid Parentheses" https://leetcode.com/problems/valid-parentheses/ """


class Solution:
    def isValid(self, s: str) -> bool:
        # (A), где A - это правильная скобочная последовательность
        # [A], где A - это правильная скобочная последовательность
        # {A}, где A - это правильная скобочная последовательность
        # (A)B, где A и B - правильные скобочные последовательности
        # [A]B, где A и B - правильные скобочные последовательности
        # {A}B, где A и B - правильные скобочные последовательности
        # Пустая скобочная последовательность - тоже правильная

        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)

            else:
                if c == ")":
                    if len(stack) != 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

                elif c == "]":
                    if len(stack) != 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False

                else:
                    if len(stack) != 0 and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0


""" 5. Решение "739. Daily Temperatures" https://leetcode.com/problems/daily-temperatures/ """


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #   0.  1.  2.  3.  4.  5.  6.  7
        # [73, 74, 75, 71, 69, 72, 76, 73]
        # [ 1,  1,  4,  2,  1,  1,  0,  0]

        # stack = []
        # i = 7, 73
        # ans[7] = 0
        # stack = [7]

        # stack = [7 (73)]
        # i = 6, 76
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[6] = 0
        # stack = [6]

        # stack = [6 (76)]
        # i = 5, 72
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[5] = 6 - 5 = 1
        # stack = [6 (76), 5 (72)]

        # stack = [6 (76), 5 (72)]
        # i = 4, 69
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[4] = 5 - 4 = 1
        # stack = [6 (76), 5 (72), 4 (69)]

        # stack = [6 (76), 5 (72), 4 (69)]
        # i = 3, 71
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[3] = 5 - 3 = 2
        # stack = [6 (76), 5 (72), 3 (71)]

        # stack = [6 (76), 5 (72), 3 (71)]
        # i = 2, 75
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[2] = 6 - 2 = 4
        # stack = [6 (76), 2 (75)]

        # stack = [6 (76), 2 (75)]
        # i = 1, 74
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[1] = 2 - 1 = 1
        # stack = [6 (76), 2 (75), 1 (74)]

        # stack = [6 (76), 2 (75), 1 (74)]
        # i = 0, 73
        # while stack and T[stack[-1]] <= T[i]: stack.pop()
        # ans[0] = 1 - 0 = 1
        # stack = [6 (76), 2 (75), 1 (74), 0 (73)]

        n = len(T)

        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i
            else:
                ans[i] = 0

            stack.append(i)

        return ans


""" 6. решение "239 Sliding Window Maximum" https://leetcode.com/problems/sliding-window-maximum/ """


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # MaxQueue with maximum in O(1)

        # How to implement queue with 2 stacks?
        # A, B = [], []
        # queue.push(x) == A.append(x)
        # queue.pop() == B.pop()
        # 7, 6, 5, 4
        # first 3 elements
        # A = [7, 6, 5], B = []
        # pop 1 element
        # A = [], B = [5, 6]
        # push next element
        # A = [4], B = [5, 6]

        # MaxStack = []
        # 5, 3, 4, 6
        # push 5
        # MaxStack = [(5, 5)]
        # push 3
        # MaxStack = [(5, 5), (3, 5)]
        # push 4
        # MaxStack = [(5, 5), (3, 5), (4, 5)]
        # push 6
        # MaxStack = [(5, 5), (3, 5), (4, 5), (6, 6)]
        # getMax()
        # print(MaxStack[-1][1])

        # 7, 6, 5, 4
        # maxA = [], maxB = []

        # push first 3 elements
        # maxA = [(7, 7), (6, 7), (5, 7)], maxB = []

        # getMax()
        # maxA[-1][1]

        # pop 1 element
        # maxA = [], maxB = [(5, 5), (6, 6)]
        # push 1 element
        # maxA = [(4, 4)], maxB = [(5, 5), (6, 6)]

        # getMax()
        # max(maxA[-1][1], maxB[-1][1])

        class MaxQueue:
            def __init__(self):
                self.a = []
                self.b = []

            def push(self, x):
                max_so_far = x

                if self.a:
                    max_so_far = max(max_so_far, self.a[-1][1])

                self.a.append((x, max_so_far))

            def pop(self):
                if not self.b:
                    while self.a:
                        x = self.a.pop()[0]

                        max_so_far = x

                        if self.b:
                            max_so_far = max(max_so_far, self.b[-1][1])

                        self.b.append((x, max_so_far))

                return self.b.pop()[0]

            def get(self):
                ans = -10 ** 100

                if self.a:
                    ans = max(ans, self.a[-1][1])

                if self.b:
                    ans = max(ans, self.b[-1][1])

                return ans


        n = len(nums)

        q = MaxQueue()

        ans = []

        for i in range(n):
            q.push(nums[i])  # O(1) amortized

            # 0, 1, 2, ..., k - 1, k, k + 1, ..., n - 1

            if i >= k - 1:
                ans.append(q.get())  # O(1) amortized
                q.pop()  # O(1) amortized

        # O(N)

        return ans