from collections import Counter, defaultdict
import numpy as np

with open('input10.txt') as f:
    numbers = list(map(int, f.read().splitlines()))

numbers_sorted = sorted(numbers)
numbers_sorted = np.array([0] + numbers_sorted + [max(numbers_sorted) + 3])
differences = Counter(numbers_sorted[1:] - numbers_sorted[:-1])

print(differences[1] * differences[3])

assert len(numbers) == len(set(numbers)), 'Numbers not disctinct'

num_paths = defaultdict(int)
num_paths[max(numbers_sorted)] = 1
for i in range(len(numbers_sorted) - 1, -1, -1):
    # Check how many later numbers this one connects to
    j = i + 1
    while j < len(numbers_sorted) and numbers_sorted[j] - numbers_sorted[i] in range(1, 4):
        num_paths[numbers_sorted[i]] += num_paths[numbers_sorted[j]]
        j += 1

print(num_paths[0])