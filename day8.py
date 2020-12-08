with open('input8.txt') as f:
    lines = [line.split(' ') for line in f.read().splitlines()]
    lines = [(op, int(value)) for (op, value) in lines]

acc, pc = 0, 0
visited_instructions = set()
while pc not in visited_instructions:
    visited_instructions.add(pc)
    op, value = lines[pc]
    if op == 'acc':
        acc += value
        pc += 1
    elif op == 'jmp':
        pc += value
    elif op == 'nop':
        pc += 1
    else:
        raise RuntimeError(f'Unknown opcode {op} in line {pc}')

print(acc)

for corrupted_line in range(len(lines)):
    acc, pc = 0, 0
    visited_instructions = set()
    while pc not in visited_instructions:
        if pc == len(lines): # Termination
            print(f'Terminated with {acc}')
            break
        else:
            visited_instructions.add(pc)
            op, value = lines[pc]
            if corrupted_line == pc and op == 'jmp':
                op = 'nop'
            elif corrupted_line == pc and op == 'nop':
                op = 'jmp'
            if op == 'acc':
                acc += value
                pc += 1
            elif op == 'jmp':
                pc += value
            elif op == 'nop':
                pc += 1
            else:
                raise RuntimeError(f'Unknown opcode {op} in line {pc}')