import sys

word = sys.stdin.readline().rstrip()
dials = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

total = 0

for each_character in word:
    for dial in dials:
        if each_character in dial:
            total += dials.index(dial) + 3

print(total)