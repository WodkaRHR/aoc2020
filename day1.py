import itertools

with open('input1.txt') as f:
    numbers = list(map(int, f.read().splitlines()))

for x, y in itertools.combinations(numbers, 2):
    if x + y == 2020:
        print(x, y, x*y)

for x, y, z in itertools.combinations(numbers, 3):
    if x + y + z == 2020:
        print(x, y, z, x * y * z)