input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for i in array:
        for compare_i in array:
            if i < compare_i:
                break
        else:
            return i


result = find_max_num(input)
print(result)