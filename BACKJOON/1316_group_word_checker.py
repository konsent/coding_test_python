import sys

n = int(sys.stdin.readline()) #변수 받아오기
total = n

for i in range(n):
    word = sys.stdin.readline()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            total -= 1
            break

print(total)