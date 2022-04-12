import sys

sentence = sys.stdin.readline().rstrip().lstrip()

word_list = sentence.split()

print(len(word_list))