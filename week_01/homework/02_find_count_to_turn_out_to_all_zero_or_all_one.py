# input = "011110"
#
#
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     string_array = []
#     idx_array = []
#     for num in string:
#         string_array.append(int(num))
#
#     for idx in range(len(string_array)-1):
#         if string_array[idx] == string_array[idx+1]:
#             if idx not in idx_array:
#                 idx_array.append(idx)
#                 idx_array.append(idx+1)
#
#     return idx_array
#     #연속된 수 찾기
#
#     #뒤집기
#     #몇 번 뒤집었는지 세기
#
# result = find_count_to_turn_out_to_all_zero_or_all_one(input)
# print(result)

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)