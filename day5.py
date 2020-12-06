def decode_binary(s, zero, one):
    return int(s.replace(zero, '0').replace(one, '1'), 2)

with open('input5.txt') as f:
    passes = [(decode_binary(p[:7], zero='F', one='B'), decode_binary(p[7:], zero='L', one='R')) for p in f.read().splitlines()]

idxs = list(map(lambda x: 8 * x[0] + x[1], passes))
print(max(idxs))

all_idxs = set(range(max(idxs) + 1))
print(all_idxs.difference(idxs))