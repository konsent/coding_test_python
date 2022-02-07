def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for i in string:
        if not i.isalpha():
            continue
        array_idx = ord(i) - ord("a")
        alphabet_occurrence_array[array_idx] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))