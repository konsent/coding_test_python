import sys

# sosu = []
# for num in range(2, 10001):
#     not_sosu = 0
#     for div in range(2, int(num ** 0.5 + 1)):
#         if num % div == 0:
#             not_sosu += 1
#     if not_sosu == 0:
#         sosu.append(num)
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     n = int(sys.stdin.readline())
#     min = 10001
#     result = 0
#     for i in sosu:
#         if i < n and n - i in sosu:
#             if abs(2 * i - n) == 0 and i == 2:
#                 print(2, 2)
#                 break
#             if abs(2 * i - n) == 0 and i == 3:
#                 print(3, 3)
#                 break
#             if abs(2 * i - n) >= min:
#                 print(result, result + min)
#                 break
#             elif abs(2 * i - n) < min:
#                 min = abs(2 * i - n)
#                 result = i

num = {x for x in range(2, 10001) if x == 2 or x % 2 == 1}
for odd in range(3,101,2):
    num -= {i for i in range(2 * odd, 10001, odd) if i in num}

T = int(sys.stdin.readline())

for _ in range(T):
    even = int(sys.stdin.readline())
    half = even // 2
    for x in range(half,1,-1):
        if (even - x in num) and (x in num):
            print(x, even-x)
            break