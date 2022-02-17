finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 내 시도 값
# def is_existing_target_number_binary(target, array):
#     target_idx = (min(array)+max(array)) // 2
#     while target != array[target_idx]:
#         if target > array[target_idx]:
#             target_idx = (max(array)+array[target_idx+1]) // 2
#         elif target < array[target_idx]:
#             target_idx = (min(array)+array[target_idx-1]) // 2
#         else:
#             break
#     return array[target_idx]

#해답
def is_existing_target_number_binary(target, array):
    current_min_idx = 0
    current_max_idx = len(array) - 1
    current_guess_idx = (current_min_idx + current_max_idx) // 2

    while current_min_idx <= current_max_idx:
        if array[current_guess_idx] == target:
            return True
        elif array[current_guess_idx] < target:
           current_min_idx = current_guess_idx + 1
        else:
            current_max_idx = current_guess_idx - 1
        current_guess_idx = (current_min_idx + current_max_idx) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)