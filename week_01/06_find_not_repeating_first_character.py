input = "abadabac"

def find_not_repeating_character(string):
    # alphabet_occurrence_array = [0] * 26
    #
    # for i in string:
    #     if not i.isalpha():
    #         continue
    #     array_idx = ord(i) - ord("a")
    #     alphabet_occurrence_array[array_idx] += 1
    #
    # not_repeating_character_array = []
    # for idx in range(len(alphabet_occurrence_array)):
    #     alphabet_occurrence = alphabet_occurrence_array[idx]
    #     if alphabet_occurrence == 1:
    #         not_repeating_character_array.append(chr(idx + ord("a")))
    #
    # for j in string:
    #     if j in not_repeating_character_array:
    #         return j
    #
    # return "_"



    # 이중 반복문 방법
    for char in string:
        repeat_count = 0
        for compare_char in string:
            if char == compare_char:
                repeat_count += 1
        if repeat_count == 1:
            return char
    return "_"



result = find_not_repeating_character(input)
print(result)