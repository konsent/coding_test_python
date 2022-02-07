input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if not i.isalpha():
            continue
        array_idx = ord(i) - ord("a")
        alphabet_occurrence_array[array_idx] += 1

    max_occurence = 0
    max_alphabet_idx = 0

    for idx in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[idx]

        if alphabet_occurrence > max_occurence:
            max_alphabet_idx = idx
            max_occurence = alphabet_occurrence

    return chr(max_alphabet_idx+97)


result = find_max_occurred_alphabet(input)
print(result)