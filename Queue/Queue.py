class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if queue.size() < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def show(self):
        print(self.queue)

    def __rep__(self):
        return str(self.queue)


queue = Queue()


def permutation(li):
    if li == [] or li is None:
        return
    if len(li) == 1:
        queue.enqueue(li[0])
        queue.show()
        queue.dequeue()
        return
    for i in range(0, len(li)):
        queue.enqueue(li[i])
        permutation(li[:i] + li[i + 1:])
        queue.dequeue()


permutation([1, 2, 3])
