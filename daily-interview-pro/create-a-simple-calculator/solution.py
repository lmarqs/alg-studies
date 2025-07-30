def recursive_eval(expression, ans=0, operation="+", i=0):
    while i < len(expression):
        c = expression[i]
        i += 1

        if c == " ":
            continue

        elif c == "(":
            [ans, i] = recursive_eval(expression, ans, operation, i)
        elif c == ")":
            break

        elif c in "+-":
            operation = c

        elif operation == "+":
            ans += int(c)

        elif operation == "-":
            ans -= int(c)

    return [ans, i]


def eval(expression):
    [ans, _] = recursive_eval(expression)
    return ans
