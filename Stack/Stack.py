class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def show(self):
        print(self.stack)

    def pop(self):
        if stack.size() < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def swap(self):
        if stack.size() > 1:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        return self.stack


stack = Stack()


def permutation(li):
    if li == [] or li is None:
        return
    if len(li) == 1:
        stack.push(li[0])
        stack.show()
        stack.pop()
        return
    for i in range(0, len(li)):
        stack.push(li[i])
        permutation(li[:i] + li[i + 1:])
        stack.pop()


permutation([1, 2, 3])
