import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

# 구글 풀이법

result = list(str(A * B * C))

for i in range(10):
    print(result.count(str(i)))



# # 나의 풀이 법
# multiplied_num = str(A * B * C)
#
# listA = [0] * 10
#
# for each_char in multiplied_num:
#     for num in range(10):
#         if int(each_char) == num:
#             listA[num] += 1
#
# for i in listA:
#     print(i)