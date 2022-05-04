graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while len(stack) > 0:
        unstacked_num = stack.pop()
        visited.append(unstacked_num)
        for adjacent_node in adjacent_graph[unstacked_num]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited



print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!