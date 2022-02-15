# input = 20
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for num in range(2, number+1):
#         for divider in range(2, num):
#             if (num % divider) == 0:
#                 break
#         else:
#             prime_list.append(num)
#
#     return prime_list
#
# result = find_prime_list_under_number(input)
# print(result)


input = 20

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i*i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)
