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

    def get_kth_node_from_last(self, k):  #내가 작성한 답
        #전체 링크드 리스트의 길이 수를 알아낸다
        count = 0
        cur = self.head
        if cur is not None:
            count += 1
        while cur.next is not None:
            count += 1
            cur = cur.next
        #링크드 리스트의 총 길이를 알아낸 뒤 뒤에서 k번째 인덱스를 조회한다
        count_idx = count - k
        cur2 = self.head
        while count_idx != 0:
            count_idx -= 1
            cur2 = cur2.next

        return cur2

    # def get_kth_node_from_last(self, k):
    #
    #     # 노드를 두 개 잡는다
    #     # 한 노드를 다른 노드보다 k 만큼 떨어지게 한다
    #     # 빠른 노드가 끝에 도달하면 느린 노드는 k 만큼 떨어져 있게 됨
    #     slow = self.head
    #     fast = self.head
    #
    #     for i in range(k): #fast를 k번 만큼 next로 이동
    #         fast = fast.next
    #
    #     while fast is not None:
    #         fast = fast.next
    #         slow = slow.next
    #
    #     return slow



linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!