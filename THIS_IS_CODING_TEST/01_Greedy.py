n = 2170


def count_number_of_each_coins(exchange_money):
    coins = [500, 100, 50, 10]
    total_count = 0
    for coin in coins:
        total_count += exchange_money // coin
        exchange_money %= coin

    return total_count

print(count_number_of_each_coins(n))