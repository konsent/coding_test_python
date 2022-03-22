n = int(input())

plans = list(input().split())


def find_final_destin(n, plans):
    x, y = 1, 1

    for plan in plans:
        if plan == 'L':
            if y == 1:
                y = 1
            else:
                y -= 1
        elif plan == 'R':
            if y == n:
                y = n
            else:
                y += 1
        elif plan == 'U':
            if x == 1:
                x = 1
            else:
                x -= 1
        elif plan == 'D':
            if x == n:
                x = n
            else:
                x += 1

    return x, y


print(find_final_destin(n, plans))
