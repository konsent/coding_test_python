import sys

word = sys.stdin.readline().rstrip()

alphabet_list = [-1] * 26
location_idx = 0

for i in word:
    idx = ord(i) - 97
    if alphabet_list[idx] == -1:
        alphabet_list[idx] = location_idx
    location_idx += 1

for j in alphabet_list:
    print(j, end=" ")