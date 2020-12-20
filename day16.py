from collections import defaultdict
import numpy as np

with open('input16.txt') as f:
    fields, my_ticket, tickets = list(map(lambda x: x.splitlines(), f.read().split('\n\n')))
    tickets = tickets[1:]
    my_ticket = list(map(int, my_ticket[1].split(',')))

field_to_values = defaultdict(set)
for field in fields:
    name, description = field.split(': ')
    values = set()
    for values in description.split(' or '):
        l, h = map(int, values.split('-'))
        field_to_values[name].update(range(l, h + 1))
    
error_rate = 0
possible_numbers = set.union(*field_to_values.values())
valid_tickets = []
for ticket in tickets[1:]:
    ticket = list(map(int, ticket.split(',')))
    invalid_values = [value for value in ticket if value not in possible_numbers]
    error_rate += sum(invalid_values)
    if len(invalid_values) == 0:
        valid_tickets.append(ticket)

print(error_rate)

valid_tickets = np.array(valid_tickets, dtype=np.int)
col_idx_to_possible_fields = {}
for col_idx, col in enumerate(valid_tickets.T):
    col_idx_to_possible_fields[col_idx] = set(name for (name, values) in field_to_values.items() if set(col).issubset(values))

# Brute force-soltuion
def brute_force(col_idx_to_possible_fields, depth=0):
    if len(col_idx_to_possible_fields) == 0:
        return []
    # Heuristic: Always try where the number of possibilities is minimal first
    min_col_idx = min(col_idx_to_possible_fields, key=lambda k: len(col_idx_to_possible_fields.get(k)))
    possible_fields = col_idx_to_possible_fields[min_col_idx]
    if len(possible_fields) == 0: # The previous assignments didn't work
        return None
    for assignment in possible_fields:
        # Assign this value to possible fields
        col_idx_to_possible_fields_new = {}
        for col_idx, possible_fields in col_idx_to_possible_fields.items():
            if col_idx != min_col_idx:
                col_idx_to_possible_fields_new[col_idx] = set(field for field in possible_fields if field != assignment)
        # print(f'assigning {assignment} to {min_col_idx}, depth {depth}')
        solution = brute_force(col_idx_to_possible_fields_new, depth=depth+1)
        if solution is not None:
            return [(min_col_idx, assignment)] + solution
    return None

field_to_col_idx = {field : col_idx for (col_idx, field) in brute_force(col_idx_to_possible_fields)}
result = 1
for field in field_to_col_idx:
    if field.startswith('departure'):
        result *= my_ticket[field_to_col_idx[field]]
print(result)