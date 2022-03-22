# 그리디 / 1이 될 때까지 p.99

n, k = map(int, input().split())
#

def make_num_1(n, k):
    count = 0
    while n != 1 and n <= k:
        if n % k == 0:
            n /= k
            count += 1
        else:
            n -= 1
            count += 1

    return count


print(make_num_1(n, k))