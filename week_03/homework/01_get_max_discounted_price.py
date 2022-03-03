shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    total = 0
    coupon_idx = 0

    if len(coupons) == 0:
        for price in prices:
            total += price
    elif len(coupons) < len(prices):
        while coupon_idx < len(coupons):
            total += prices[coupon_idx] * (1 - coupons[coupon_idx]/100)
            coupon_idx += 1
        for i in range(len(coupons), len(prices)):
            total += prices[i]
    else:
        for price in prices:
            total += price * (1 - coupons[coupon_idx] / 100)
            coupon_idx += 1
    return int(total)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
