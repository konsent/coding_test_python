import sys

N = int(sys.stdin.readline())


def star_sqr(n):
    if n == 1:
        return ['*']

    stars = star_sqr(n // 3)
    result_grid = []

    for star in stars:
        result_grid.append(star * 3)
    for star in stars:
        result_grid.append(star + ' ' * (n // 3) + star)
    for star in stars:
        result_grid.append(star * 3)

    return result_grid


print('\n'.join(star_sqr(N)))
