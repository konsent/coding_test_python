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

# #   나의 풀이 법
#     def add_node(self, index, value):
#         count_num = index # 인덱스를 count 변수에 저장
#         cur = self.head
#         while count_num > 1:  # 0번쨰의 예외처리가 안되어 있음
#             cur = cur.next
#             count_num -= 1
#         temp_cur = cur.next # 원하는 인덱스 다음 번 노드를 임시 저장소에 저장
#         cur.next = Node(value) # 원하는 인덱스에 value 노드를 저장
#         cur.next.next = temp_cur # 임시 저장소에 있던 그 다음 노드를 다시 가져와 연결
#         return cur.next.data

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


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(0,6)
linked_list.print_all()