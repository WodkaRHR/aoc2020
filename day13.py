import numpy as np
from egcd import egcd

with open('input13.txt') as f:
    arrival, busses = f.read().splitlines()
arrival = int(arrival)
busses = [int(b) for b in busses.split(',') if b != 'x']

missed = {b : arrival % b for b in busses} # How many minutes arrival is later than a bus
wait = {b : -m % b for (b, m) in missed.items()}
for b, w in wait.items():
    if w == min(wait.values()):
        print(b, w, b * w)

with open('input13.txt') as f:
    arrival, busses = f.read().splitlines()
    busses = [(int(b), (-t) % int(b)) for (t, b) in enumerate(busses.split(',')) if b != 'x']

# Tuples (a, b) s.t. T = b (mod a)
# Find a solution to this system using Chinese Remainder Theorem

lcm = np.lcm.reduce([b for (b, t) in busses])
T = 0
for b, t in busses:
    M = lcm // b
    _, r, s = egcd(b, M)
    T += t * s * M
print(T % lcm)