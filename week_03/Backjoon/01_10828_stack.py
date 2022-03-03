import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
         new_head = Node(value)
         new_head.next = self.head
         self.head = new_head

    def pop(self):
        if self.is_empty():
            return -1
        del_head = self.head
        self.head = self.head.next
        return del_head

    def size(self):
        cur = self.head
        size = 0
        if cur is None:
            return 0
        else:
            size += 1
        while cur.next is not None:
            size += 1
            cur = cur.next
        return size

    def top(self):
        if self.is_empty():
            return -1
        return self.head

    def is_empty(self):
        if self.head is None:
            return 1
        else:
            return 0


# n = int(sys.stdin.readline())
# stack = Stack()
# for i in range(n):
#     command = sys.stdin.readline().split()
#
#     if command[0] == 'push':
#         stack.push(command[1])
#     elif command[0] == 'pop':
#         stack.pop()
#     elif command[0] == 'size':
#         stack.size()
#     elif command[0] == 'top':
#         stack.top()
#     elif command[0] == 'empty':
#         stack.is_empty()
#

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())
