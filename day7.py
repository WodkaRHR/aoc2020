from collections import defaultdict

edges = defaultdict(dict)
edges_rev = defaultdict(dict)

with open('input7.txt') as f:
    for line in f.read().replace(' bags', '').replace(' bag', '').replace('.', '').splitlines():
        bag, targets = line.split(' contain ')
        for target in targets.split(', '):
            if target != 'no other':
                count, other = target.split(' ', 1)
                edges[bag][other] = int(count)
                edges_rev[other][bag] = int(count)

# Reachability on reveresed graph
todo = ['shiny gold']
visited = set()
while len(todo) > 0:
    next = todo.pop(0)
    if next in visited:
        continue
    visited.add(next)
    for pred in edges_rev[next]:
        if pred not in visited:
            todo.append(pred)
print(len(visited) - 1)

def size(bag, egdes):
    if bag not in edges:
        return 0
    else:
        _size = 0
        for next in edges[bag]:
            _size += (1 + size(next, edges)) * edges[bag][next] # assumes no cycles here though...
        return _size
print(size('shiny gold', edges))