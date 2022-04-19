# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min = self.min[:-1]

        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(2)
    print(obj.min)
    obj.push(-2)
    print(obj.min)