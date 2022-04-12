import sys

word = sys.stdin.readline().rstrip()
char_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
new_word = word

for char in char_list:
    new_word = new_word.replace(char,"*")

print(len(new_word))
