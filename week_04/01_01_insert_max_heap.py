# class MaxHeap:
#     def __init__(self):
#         self.items = [None]
#
#     def insert(self, value):
#         if len(self.items) == 1:
#             self.items.append(value)
#         else:
#             new_num_idx = len(self.items)
#             parent_idx = new_num_idx // 2
#             self.items.append(value)
#
#             while self.items[parent_idx] < self.items[new_num_idx]:
#                 tmp = self.items[parent_idx]
#                 self.items[parent_idx] = value
#                 self.items[new_num_idx] = tmp
#                 if new_num_idx > 2:
#                     new_num_idx = parent_idx
#                     parent_idx = new_num_idx // 2
#
#         return

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_idx = len(self.items) - 1

        while cur_idx > 1:
            parent_idx = cur_idx // 2
            if self.items[parent_idx] < self.items[cur_idx]:
                self.items[parent_idx],self.items[cur_idx] = self.items[cur_idx],self.items[parent_idx]
                cur_idx = parent_idx
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)  # [None, 3]
max_heap.insert(4)  # [None, 4, 3]
max_heap.insert(2)  # [None, 4, 3, 2]
max_heap.insert(9)  # [None, 4, 9, 2, 3]
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
