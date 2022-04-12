import sys

word = sys.stdin.readline().rstrip().lower()
unique_word = list(set(word))

count_list = []

for x in unique_word:
    count = word.count(x)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_idx = count_list.index(max(count_list))
    print(unique_word[max_idx].upper())