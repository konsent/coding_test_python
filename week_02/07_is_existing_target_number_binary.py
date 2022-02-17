finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

#나의 풀이
def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    min_idx = 0
    max_idx = len(numbers) - 1
    target_idx = (max_idx + min_idx) // 2

    while min_idx <= max_idx:
        if numbers[target_idx] < target:
            min_idx = target_idx + 1
        elif numbers[target_idx] > target:
            max_idx = target_idx - 1
        else:
            return True
        target_idx = (min_idx + max_idx) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)