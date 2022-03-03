from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []

    while prices:
        count = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price <= next_price:
                count += 1
            count += 1
            break

        answer.append(count)

    return answer


print("정답 = [2, 1, 2, 1, 0] / 현재 풀이 값 = ",solution([6,9,5,7,4]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ",solution([3,9,9,3,5,7,2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ",solution([1,5,3,6,7,6,5]))