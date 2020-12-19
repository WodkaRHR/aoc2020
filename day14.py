from collections import defaultdict
import itertools

with open('input14.txt') as f:
    lines = f.read().splitlines()

memory = defaultdict(int)
mask, apply = 0, 0

for line in lines:
    command, value = line.split(' = ')
    if command == 'mask':
        mask = ~int(value.replace('0', '1').replace('X', '0'), 2)
        apply = int(value.replace('X', '0'), 2)
    else:
        addr = command[4:-1]
        value = mask & int(value, 10)
        value |= apply
        memory[addr] = value

print(sum(memory.values()))

memory = defaultdict(int)
mask_idxs, or_mask = [], 0

for line in lines:
    command, value = line.split(' = ')
    if command == 'mask':
        or_mask = int(value.replace('X', '0'), 2)
        mask_idxs = [idx for (idx, c) in enumerate(value) if c == 'X']
    else:
        base_addr = bin(int(command[4:-1], 10) | or_mask)[2:].zfill(36)
        # Write to all addresses
        for values in itertools.product(range(2), repeat=len(mask_idxs)):
            addr = list(base_addr)
            for idx, bit in zip(mask_idxs, values):
                addr[idx] = str(bit)
            memory[int("".join(addr), 2)] = int(value)

print(sum(memory.values()))