from collections import defaultdict

with open('input19.txt') as f:
    rule_lines, lines = list(map(lambda x: x.splitlines(), f.read().split('\n\n')))

rules = defaultdict(set)
for line in rule_lines:
    num, rule = line.split(': ')
    num = int(num)
    if '"' in rule:
        rules[num].add(rule[1:-1])
    else:
        for sequence in rule.split(' | '):
            rules[num].add(tuple(map(int, sequence.split(' '))))

def matches(x, rule):
    """ Returns how many chars of x could be matched by rule """
    # print(f'Matches "{x}" to {rule}?"')
    if len(x) == 0:
        return set()
    if isinstance(rule, str):
        if x[0] == rule:
            return set((1, ))
        else:
            return set()
    elif isinstance(rule, set):
        # A set of rules, any of which could match (a possibly different) number of chars
        possible_matches = set()
        for subrule in rule:
            possible_matches.update(matches(x, subrule))
        return possible_matches
    elif isinstance(rule, tuple):
        # A sequence of rules that must match
        match_first = matches(x, rules[rule[0]])
        if len(rule) == 1:
            return match_first
        else:
            match_all = set()
            for num_matched in match_first:
                match_next = matches(x[num_matched : ], rule[1:])
                match_all.update(num_matched + num_next for num_next in match_next)
            return match_all

print(len( [line for line in lines if len(line) in matches(line, rules[0]) ] ))

rules[8] = {(42, ), (42, 8)}
rules[11] = {(42, 31), (42, 11, 31)}

print(len( [line for line in lines if len(line) in matches(line, rules[0]) ] ))
