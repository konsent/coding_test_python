class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        count_num = index
        cur = self.head
        while count_num != 0:
            cur = cur.next
            count_num -= 1
        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

#   나의 풀이법
    def delete_node(self, index):
        next_node = self.get_node(index).next
        if index == 0:
            self.head = next_node
            return # return을 작성하지 않으면 하위 코드가 실행되므로 꼭 작성!!

        prev_node = self.get_node(index-1)
        prev_node.next = next_node



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(0,6)
linked_list.delete_node(0)
linked_list.print_all()
