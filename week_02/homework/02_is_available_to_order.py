shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


# def is_existing_target_number_binary(target, array):
#     min_idx = 0
#     max_idx = len(array) - 1
#     guess_idx = (min_idx + max_idx) // 2
#     while min_idx <= max_idx:
#         if array[guess_idx] < target:
#             min_idx = guess_idx + 1
#         elif array[guess_idx] > target:
#             max_idx = guess_idx - 1
#         else:
#             return True
#         guess_idx = (min_idx + max_idx) // 2
#     return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)

