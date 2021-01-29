class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    # Show all the element
    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end='')
            curr = curr.next

    # Display total number of elements
    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count

    # Push an element in the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Pop an element from the stack
    def pop(self):
        if self.size() == 0:
            print('all the elements are popped')
        else:
            self.head = self.head.next


# Create an object link
link = Linked()


def permutation(li):
    if len(li) == 1:
        link.push(li[0])
        link.show()
        print(' ', end='')
        link.pop()
        return
    for i in range(0, len(li)):
        link.push(li[i])
        permutation(li[:i] + li[i + 1:])
        link.pop()


permutation([1, 2, 3])
