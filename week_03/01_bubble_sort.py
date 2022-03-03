input = [4, 6, 2, 9, 1]

# # 내 답안
# def bubble_sort(array):
#     for times in range(len(array) - 1):
#         for i in range(len(array)-1):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#
#     return array

def bubble_sort(array):
    n = len(array)
    for i in range(n- 1):
        for j in range(n - 1- i): #한 번 돌 때마다 맨 마지막 숫자는 정렬되기 때문에 마지막꺼는 다음에 정렬 안해도 됨
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!