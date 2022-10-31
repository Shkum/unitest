def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError\
            (f'Expression should have one of following signs "{allowed}"')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = map(int, expression.split(sign))
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '/': lambda a, b: a / b,
                    '*': lambda a, b: a * b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Expression should contain two integers and one sign')


if __name__ == '__main__':
    print(calculator('1545*546'))

