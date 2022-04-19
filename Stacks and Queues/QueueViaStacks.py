# https://leetcode.com/problems/implement-queue-using-stacks/

from collections import deque

# class MyQueue:
#
#     def __init__(self):
#         self.main = []
#         self.dop = []
#
#     def push(self, x: int) -> None:
#         if len(self.main) == 0:
#             self.main.append(x)
#         else:
#             for i in range(len(self.main)):
#                 self.dop.append(self.main.pop())
#
#             self.main.append(x)
#
#             for i in range(len(self.dop)):
#                 self.main.append(self.dop.pop())
#
#     def pop(self) -> int:
#         return self.main.pop() if len(self.main) != 0 else -1
#     def peek(self) -> int:
#         return self.main[-1] if len(self.main) != 0 else None
#     def empty(self) -> bool:
#         return len(self.main) == 0
#
#     def print(self):
#         print(self.main)

class MyQueue:

    def __init__(self):
        self.main = deque()

    def push(self, x: int) -> None:
        self.main.appendleft(x)

    def pop(self) -> int:
        return self.main.popleft()

    def peek(self) -> int:
        return self.main[-1] if len(self.main) != 0 else None

    def empty(self) -> bool:
        return len(self.main) == 0

    def print(self):
        print(self.main)

if __name__ == '__main__':
    obj = MyQueue()
    obj.print()
    obj.push(1)
    obj.print()
    obj.push(2)
    obj.print()
    obj.push(3)
    obj.print()
    obj.push(4)
    obj.print()
    obj.push(5)
    obj.print()
    obj.push(6)
    obj.print()
    obj.pop()
    obj.print()
