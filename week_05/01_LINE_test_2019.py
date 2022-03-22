from collections import deque

c = 11
b = 2


# 1초씩 반복해서
# 코니가 움직인 거리와 브라운이 움직인 거리가 같을 때를 반환
# 코니가 움직인 거리 : C+(n(n+1)/2)
# 브라운이 움직인 거리


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))

    while 0 <= cony_loc <= 200000:
        cony_loc += time

        for i in range(0, len(queue)):
            cur_position, cur_time = queue.popleft()

            new_time = cur_time + 1

            new_position = cur_position - 1
            queue.append((new_position, new_time))

            new_position = cur_position + 1
            queue.append((new_position, new_time))

            new_position = cur_position * 2
            queue.append((new_position, new_time))

        time += 1





print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
