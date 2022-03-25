import sys


listA = []

for i in range(10):
    input_num = int(sys.stdin.readline())
    listA.append(input_num % 42)

listA_set = set(listA)
print(len(listA_set))