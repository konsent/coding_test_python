s = "(())()"


def is_correct_parenthesis(string):
    stack = []
    for p in string:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False






print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!