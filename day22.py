with open('input22.txt') as f:
    deck1, deck2 = list(map(lambda deck: list(map(int, deck.splitlines()[1:])), f.read().split('\n\n')))

while len(deck1) and len(deck2):
    a, b = deck1.pop(0), deck2.pop(0)
    if a > b:
        deck1 += [a, b]
    elif b > a:
        deck2 += [b, a]
    else:
        raise RuntimeError(f'Cards of equal rank {a}, {b}')

print(sum((idx + 1) * card for (idx, card) in enumerate(deck1[::-1] + deck2[::-1])  ))

with open('input22.txt') as f:
    deck1, deck2 = list(map(lambda deck: list(map(int, deck.splitlines()[1:])), f.read().split('\n\n')))

def configuration_to_tuple(deck1, deck2):
    return tuple((tuple(deck1), tuple(deck2)))

def recursive_game(deck1, deck2, depth=1):
    configurations = set()
    while len(deck1) and len(deck2):
        current = configuration_to_tuple(deck1, deck2)
        if current in configurations:
            return [None], [] # Player 1 wins?
        configurations.add(current)
        # print(f'Depth {depth}')
        # print(f'Player 1 deck: {deck1}')
        # print(f'Player 2 deck: {deck2}')
        a, b = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= a and len(deck2) >= b:
            # print(f'Play subgame...')
            sub1, sub2 = recursive_game(deck1[:a], deck2[:b], depth=depth+1)
            rank1, rank2 = len(sub1), len(sub2)
        else:
            rank1, rank2 = a, b
        if rank1 > rank2:
            deck1 += [a, b]
        elif rank2 > rank1:
            deck2 += [b, a]
        else:
            raise RuntimeError(f'Cards of equal rank {a}, {b}')
    return deck1, deck2 

deck1, deck2 = recursive_game(deck1, deck2)
print(sum((idx + 1) * card for (idx, card) in enumerate(deck1[::-1] + deck2[::-1])  ))





