knight_location = input()

row = int(knight_location[1])
column = int(ord(knight_location[0])) - 96

plans = [(2, 1), (2, -1), (-1, 2), (1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
count = 0
for plan in plans:
    next_row = row + plan[1]
    next_column = column + plan[0]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)