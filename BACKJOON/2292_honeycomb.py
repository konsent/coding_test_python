import sys
#
# N = int(sys.stdin.readline())
#
# n = 0
# min1 = 2
# while True:
#     min1 += 6 * n
#     max1 = min1 + (6 * (n + 1))
#     if min1 <= N < max1:
#         print(n + 2)
#         break
#     else:
#         n += 1

N = int(sys.stdin.readline())

room_count = 1
increased_rooms = 6
count = 1
while N > room_count:
    count += 1
    room_count += increased_rooms
    increased_rooms += 6

print(count)