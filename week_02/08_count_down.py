def count_down(number):
    while number >= 0:
        print(number)          # number를 출력하고
        number -= 1 # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)

def count_down(number):
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)