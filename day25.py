k1 = 12090988
k2 = 240583
p = 20201227

n, x = 0, 1
x1, x2 = 1, 1
r1, r2 = None, None
while r1 is None or r2 is None:
    x = (x * 7) % p
    x1 = (x1 * k1) % p
    x2 = (x2 * k2) % p
    n += 1
    if x == k1:
        r2 = x2
    elif x == k2:
        r1 = x1

assert r1 == r2
print(r1)
