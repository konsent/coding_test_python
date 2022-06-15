import math
import sys

n = int(sys.stdin.readline())

# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n-1)

# def fac1(n):
#     factorial = 1
#     for i in range(n,0,-1):
#         factorial *= i
#     return factorial



def get_fac0(n):
    strA = str(math.factorial(n))
    count = 0
    for i in range(len(strA)-1,-1,-1):
        if int(strA[i]) != 0:
            return count
        else:
            count += 1
    return count


print(get_fac0(n))
