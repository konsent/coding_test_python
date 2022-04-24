import sys

N = int(sys.stdin.readline()) #N번째 수

count = 0
n = 666
while count < N:
    if str(n).find("666") >= 0:
        count += 1
    n += 1

# while 1:
#     if str(n).find("666") >= 0:
#         count += 1
#         if count == N:
#             break
#     n += 1

print(n - 1)