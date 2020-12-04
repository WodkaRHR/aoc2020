from collections import Counter

with open('input2.txt') as f:
    lines = f.read().splitlines()

num_valid = 0
for line in lines:
    limits, letter, pwd = line.split(' ')
    lmin, lmax = list(map(int, limits.split('-')))
    counts = Counter(pwd)
    if counts[letter[:1]] in range(lmin, lmax + 1):
        num_valid += 1
print(num_valid)

num_valid = 0
for line in lines:
    limits, letter, pwd = line.split(' ')
    i, j = list(map(int, limits.split('-')))
    letter = letter[:1]
    num_occurences = (pwd[i - 1] == letter) + (pwd[j - 1] == letter)
    if num_occurences == 1:
        num_valid += 1
print(num_valid)