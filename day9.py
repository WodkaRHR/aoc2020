import itertools

with open('input9.txt') as f:
    numbers = list(map(int, f.read().splitlines()))

invalid_idx, invalid_number = None, None

window_size = 25
for idx in range(window_size, len(numbers)):
    previous = set(x + y for (x, y) in itertools.combinations(numbers[idx - 25 : idx], 2))
    if numbers[idx] not in previous:
        invalid_idx, invalid_number = idx, numbers[idx]

print(invalid_number)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        r = numbers[i : j]
        if sum(r) == invalid_number:
            print(min(r) + max(r))


