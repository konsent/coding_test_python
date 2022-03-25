import sys


N = int(sys.stdin.readline())
grades = list(map(int, sys.stdin.readline().split()))

max_grade = max(grades)
result = 0

for grade in grades:
    result += grade / max_grade * 100 / len(grades)

print(result)