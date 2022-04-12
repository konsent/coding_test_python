all_int = set(range(1,10000))
not_self_num = set()

for i in range(1, 10001):
    for each_num in str(i):
        i += int(each_num)
    not_self_num.add(i)


self_num = sorted(all_int - not_self_num)
for i in self_num:
    print(i)

