from collections import deque

queue1 = [1, 1]
queue2 = [1, 5]


def solution(queue1, queue2):
    sumA = (sum(queue1) + sum(queue2))
    goal = sumA / 2

    q1 = deque(queue1)
    q2 = deque(queue2)

    count = 0
    while True:
        if max(max(q1),max(q2)) > sumA - max(max(q1),max(q2)):
            return -1

        if sum(q1) > goal:
            q2.append(q1.popleft())
            count += 1
        elif goal > sum(q1):
            q1.append(q2.popleft())
            count += 1
        else:
            return count



print(solution(queue1, queue2))