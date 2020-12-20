from functools import reduce
import operator

with open('input18.txt') as f:
    # Let python do the parsing work for me?
    lines = [
        eval('[' + line.replace(' ', '').replace('+', ',"+",').replace('*', ',"*",').replace('(', '[').replace(')', ']') + ']') for line in f.read().splitlines()
    ]

def solve(expr):
    if isinstance(expr, int):
        return expr
    elif len(expr) == 1:
        return solve(expr[0])
    elif isinstance(expr, list):
        b = solve(expr[-1])
        op = expr[-2]
        a = solve(expr[:-2])
        if op == '*':
            return a * b
        elif op == '+':
            return a + b

print(sum(map(solve, lines)))

def solve2(expr):
    if isinstance(expr, int):
        return expr
    elif len(expr) == 1:
        return solve(expr[0])
    else:
        # Resolve all brackets
        expr = [solve2(sub) if sub not in ('*', '+') else sub for sub in expr]
        while '+' in expr:
            idx = expr.index('+')
            a, b = expr[idx - 1], expr[idx + 1]
            expr = expr[: idx - 1] + [a + b] + expr[idx + 2 : ]
        # Now only * is left, we can just multiply all of them together
        return reduce(operator.mul, expr[::2], 1)

print(sum(map(solve2, lines)))
        

