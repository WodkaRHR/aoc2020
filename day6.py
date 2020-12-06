import functools
import string

with open('input6.txt') as f:
    groups = [[set(answers) for answers in group.splitlines()] for group in f.read().split('\n\n')]
    groups_union = [functools.reduce(lambda a, b: a.union(b), group, set()) for group in groups]
    groups_intersection = [functools.reduce(lambda a, b: a.intersection(b), group, set(string.ascii_lowercase)) for group in groups]
    
print(sum(map(lambda group: len(group), groups_union)))
print(sum(map(lambda group: len(group), groups_intersection)))