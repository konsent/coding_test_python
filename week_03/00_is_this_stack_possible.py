

def stack_sequence(n, sequence):
    stack = []
    num = 1
    idx = 0
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1
        elif stack[-1] == sequence[idx]:
            stack.pop()
            result.append("-")
            idx += 1
            if idx == n:
                break
        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for char in result:
            print(char)

n = int(input())
sequence = list()
for i in range(n):
    sequence.append(int(input()))


stack_sequence(n, sequence)


