input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break

    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
            cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next