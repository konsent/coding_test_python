n, m, k = map(int, input().split())
data = list(map(int, input().split()))
# 배열의 크기 n, 숫자가 더해지는 횟수 m, 연속 덧셈 가능한 횟수 k
# m = 8, k =3
# 2 2 2 1 2 2 2 1

data.sort()



# l은 m%k번
# 가장 큰 수 L, 두번쨰 큰 수 l
largest_num = data[-1]
second_num = data[-2]

total = 0
# L*k는 m//k번 더해진다
total += largest_num * k * (m // k)
total += second_num * (m % k)

print(total)